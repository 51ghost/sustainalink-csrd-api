"""Sustainability metrics CRUD routes."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import MetricModel
from src.database.session import get_db
from src.schemas.responses import MetricCreateRequest, MetricResponse, MetricListResponse

router = APIRouter()


@router.post("/metrics", response_model=MetricResponse, status_code=201)
async def create_metric(req: MetricCreateRequest, db: AsyncSession = Depends(get_db)):
    """Record a new sustainability metric value for an ESRS datapoint."""
    metric = MetricModel(
        datapoint_id=req.datapoint_id,
        standard_id=req.standard_id,
        value=req.value,
        unit=req.unit,
        period_start=req.period_start,
        period_end=req.period_end,
        source=req.source,
        metadata_=req.metadata,
    )
    db.add(metric)
    await db.flush()
    return MetricResponse(
        id=metric.id,
        datapoint_id=metric.datapoint_id,
        standard_id=metric.standard_id,
        value=metric.value,
        unit=metric.unit,
        period_start=metric.period_start,
        period_end=metric.period_end,
        source=metric.source,
        metadata=metric.metadata_,
        created_at=metric.created_at,
        updated_at=metric.updated_at,
    )


@router.get("/metrics", response_model=MetricListResponse)
async def list_metrics(
    standard_id: Optional[str] = None,
    datapoint_id: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    """List recorded sustainability metrics with optional filters."""
    stmt = select(MetricModel).order_by(MetricModel.created_at.desc())
    if standard_id:
        stmt = stmt.where(MetricModel.standard_id == standard_id.upper())
    if datapoint_id:
        stmt = stmt.where(MetricModel.datapoint_id == datapoint_id.upper())

    result = await db.execute(stmt.offset(offset).limit(limit))
    rows = result.scalars().all()

    # Count total
    count_stmt = select(func.count()).select_from(MetricModel)
    if standard_id:
        count_stmt = count_stmt.where(MetricModel.standard_id == standard_id.upper())
    if datapoint_id:
        count_stmt = count_stmt.where(MetricModel.datapoint_id == datapoint_id.upper())
    count_result = await db.execute(count_stmt)
    total = count_result.scalar() or 0

    return MetricListResponse(
        total=total,
        metrics=[
            MetricResponse(
                id=m.id,
                datapoint_id=m.datapoint_id,
                standard_id=m.standard_id,
                value=m.value,
                unit=m.unit,
                period_start=m.period_start,
                period_end=m.period_end,
                source=m.source,
                metadata=m.metadata_,
                created_at=m.created_at,
                updated_at=m.updated_at,
            )
            for m in rows
        ],
    )


@router.get("/metrics/{metric_id}", response_model=MetricResponse)
async def get_metric(metric_id: str, db: AsyncSession = Depends(get_db)):
    """Get a specific recorded metric by its ID."""
    result = await db.execute(select(MetricModel).where(MetricModel.id == metric_id))
    metric = result.scalar_one_or_none()
    if not metric:
        raise HTTPException(status_code=404, detail=f"Metric '{metric_id}' not found")
    return MetricResponse(
        id=metric.id,
        datapoint_id=metric.datapoint_id,
        standard_id=metric.standard_id,
        value=metric.value,
        unit=metric.unit,
        period_start=metric.period_start,
        period_end=metric.period_end,
        source=metric.source,
        metadata=metric.metadata_,
        created_at=metric.created_at,
        updated_at=metric.updated_at,
    )
