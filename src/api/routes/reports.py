"""Report generation routes."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import MetricModel, ReportModel
from src.database.session import get_db
from src.schemas.responses import ReportDraftRequest, ReportResponse, ReportListResponse
from src.services.reporting_service import generate_report_content

router = APIRouter()


@router.post("/reports/draft", response_model=ReportResponse, status_code=201)
async def draft_report(req: ReportDraftRequest, db: AsyncSession = Depends(get_db)):
    """Generate a draft CSRD sustainability report from recorded metrics.

    The report is assembled by collecting all metrics (optionally filtered
    by standard) and organizing them by ESRS standard category.
    """
    # Fetch metrics, optionally filtered by standard
    stmt = select(MetricModel).order_by(MetricModel.standard_id, MetricModel.datapoint_id)
    if req.include_standards:
        stmt = stmt.where(MetricModel.standard_id.in_([s.upper() for s in req.include_standards]))
    result = await db.execute(stmt)
    metrics = result.scalars().all()

    if not metrics:
        raise HTTPException(status_code=400, detail="No metrics found for the specified standards. Record metrics first.")

    # Build report content
    content = generate_report_content(metrics, title=req.title)

    report = ReportModel(
        title=req.title,
        status="draft",
        reporting_period=req.reporting_period,
        metrics_used=[m.id for m in metrics],
        content=content,
        version=req.version or "0.1.0",
    )
    db.add(report)
    await db.flush()

    return ReportResponse(
        id=report.id,
        title=report.title,
        status=report.status,
        reporting_period=report.reporting_period,
        metrics_used=report.metrics_used,
        content=report.content,
        version=report.version,
        created_at=report.created_at,
        updated_at=report.updated_at,
    )


@router.get("/reports", response_model=ReportListResponse)
async def list_reports(limit: int = 20, offset: int = 0, db: AsyncSession = Depends(get_db)):
    """List all generated CSRD reports."""
    result = await db.execute(
        select(ReportModel).order_by(ReportModel.created_at.desc()).offset(offset).limit(limit)
    )
    reports = result.scalars().all()

    count_result = await db.execute(select(select(ReportModel).count().label("total")))
    total = count_result.scalar() or 0

    return ReportListResponse(
        total=total,
        reports=[
            ReportResponse(
                id=r.id,
                title=r.title,
                status=r.status,
                reporting_period=r.reporting_period,
                metrics_used=r.metrics_used,
                content=r.content,
                version=r.version,
                created_at=r.created_at,
                updated_at=r.updated_at,
            )
            for r in reports
        ],
    )


@router.get("/reports/{report_id}", response_model=ReportResponse)
async def get_report(report_id: str, db: AsyncSession = Depends(get_db)):
    """Get a specific report by its ID."""
    result = await db.execute(select(ReportModel).where(ReportModel.id == report_id))
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail=f"Report '{report_id}' not found")
    return ReportResponse(
        id=report.id,
        title=report.title,
        status=report.status,
        reporting_period=report.reporting_period,
        metrics_used=report.metrics_used,
        content=report.content,
        version=report.version,
        created_at=report.created_at,
        updated_at=report.updated_at,
    )
