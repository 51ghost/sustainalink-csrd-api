"""ESRS standards and datapoints routes."""

from typing import Optional
from fastapi import APIRouter, HTTPException

from config.esrs_data import ESRS_STANDARDS, DATAPOINTS
from src.schemas.responses import (
    ESRSStandardResponse,
    ESRSStandardListResponse,
    ESRSDatapointResponse,
    ESRSDatapointListResponse,
)

router = APIRouter()


@router.get("/esrs/standards", response_model=ESRSStandardListResponse)
async def list_standards(category: Optional[str] = None):
    """List all ESRS standards, optionally filtered by category."""
    standards = ESRS_STANDARDS
    if category:
        standards = [s for s in standards if s["category"] == category]
    return ESRSStandardListResponse(
        total=len(standards),
        standards=[ESRSStandardResponse(**s) for s in standards],
    )


@router.get("/esrs/standards/{standard_id}", response_model=ESRSStandardResponse)
async def get_standard(standard_id: str):
    """Get a specific ESRS standard by its ID (e.g. ESRS_E1)."""
    for s in ESRS_STANDARDS:
        if s["id"] == standard_id.upper():
            return ESRSStandardResponse(**s)
    raise HTTPException(status_code=404, detail=f"ESRS standard '{standard_id}' not found")


@router.get("/esrs/datapoints", response_model=ESRSDatapointListResponse)
async def list_datapoints(standard: Optional[str] = None):
    """List all ESRS datapoints, optionally filtered by standard ID."""
    dps = list(DATAPOINTS.values())
    if standard:
        dps = [dp for dp in dps if dp["standard"] == standard.upper()]
    return ESRSDatapointListResponse(
        total=len(dps),
        datapoints=[ESRSDatapointResponse(id=k, **v) for k, v in DATAPOINTS.items() if not standard or v["standard"] == standard.upper()],
    )


@router.get("/esrs/datapoints/{datapoint_id}", response_model=ESRSDatapointResponse)
async def get_datapoint(datapoint_id: str):
    """Get a specific ESRS datapoint by its ID (e.g. DP-E1-1)."""
    dp = DATAPOINTS.get(datapoint_id.upper())
    if not dp:
        raise HTTPException(status_code=404, detail=f"Datapoint '{datapoint_id}' not found")
    return ESRSDatapointResponse(id=datapoint_id.upper(), **dp)
