"""CSRD compliance assessment route."""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.esrs_data import ESRS_STANDARDS, DATAPOINTS
from src.database.models import MetricModel
from src.database.session import get_db
from src.schemas.responses import (
    ComplianceAssessmentRequest,
    ComplianceAssessmentResponse,
    ComplianceCategoryScore,
)

router = APIRouter()


@router.post("/compliance/assess", response_model=ComplianceAssessmentResponse)
async def assess_compliance(req: ComplianceAssessmentRequest, db: AsyncSession = Depends(get_db)):
    """Run a CSRD compliance assessment comparing recorded metrics against ESRS requirements.

    Returns a gap analysis with per-category scores and actionable recommendations.
    """
    # Determine which standards to assess
    standards = ESRS_STANDARDS
    if req.standard_ids:
        ids = [s.upper() for s in req.standard_ids]
        standards = [s for s in standards if s["id"] in ids]

    # Gather all required datapoints
    all_required_dps: list[str] = []
    for s in standards:
        all_required_dps.extend(s["datapoints"])

    # Fetch existing metrics from DB
    stmt = select(MetricModel)
    result = await db.execute(stmt)
    existing_metrics = result.scalars().all()

    recorded_dps: set[str] = {m.datapoint_id for m in existing_metrics}

    # Calculate per-category scores
    category_results: dict[str, dict] = {}
    for s in standards:
        cat = s["category"]
        if cat not in category_results:
            category_results[cat] = {"total": 0, "completed": 0}
        for dp_id in s["datapoints"]:
            category_results[cat]["total"] += 1
            if dp_id in recorded_dps:
                category_results[cat]["completed"] += 1

    category_scores = []
    for cat, counts in category_results.items():
        score = (counts["completed"] / counts["total"] * 100) if counts["total"] > 0 else 0.0
        if score == 100:
            status = "compliant"
        elif score >= 50:
            status = "partially_compliant"
        else:
            status = "non_compliant"
        category_scores.append(
            ComplianceCategoryScore(
                category=cat,
                total_datapoints=counts["total"],
                completed_datapoints=counts["completed"],
                score_percent=round(score, 1),
                status=status,
            )
        )

    # Overall metrics
    total_dps = sum(c["total"] for c in category_results.values())
    completed_dps = sum(c["completed"] for c in category_results.values())
    overall_score = (completed_dps / total_dps * 100) if total_dps > 0 else 0.0

    if overall_score == 100:
        overall_status = "compliant"
    elif overall_score >= 50:
        overall_status = "partially_compliant"
    else:
        overall_status = "non_compliant"

    # Missing datapoints
    missing = [dp for dp in all_required_dps if dp not in recorded_dps]

    # Generate recommendations
    recommendations = []
    if missing:
        recommendations.append(f"Record data for {len(missing)} missing datapoint(s): {', '.join(missing[:10])}" + ("..." if len(missing) > 10 else ""))
    low_cats = [cs for cs in category_scores if cs.score_percent < 50]
    for lc in low_cats:
        recommendations.append(f"Focus on {lc.category} category — only {lc.score_percent}% complete.")
    if overall_score >= 75:
        recommendations.append("Good progress — continue collecting data for remaining non-compliant areas.")
    recommendations.append("Review ESRS disclosure requirements for completeness and data quality.")

    return ComplianceAssessmentResponse(
        reporting_period=req.reporting_period,
        overall_score=round(overall_score, 1),
        overall_status=overall_status,
        total_datapoints=total_dps,
        completed_datapoints=completed_dps,
        categories=category_scores,
        missing_datapoints=missing,
        recommendations=recommendations,
    )
