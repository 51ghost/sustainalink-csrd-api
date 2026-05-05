"""Pydantic request/response schemas for the SustainaLink CSRD API."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


# --- Health ---

class HealthResponse(BaseModel):
    status: str
    version: str
    service: str


# --- ESRS ---

class DisclosureRequirement(BaseModel):
    id: str
    title: str
    description: str


class ESRSStandardResponse(BaseModel):
    id: str
    name: str
    category: str
    description: str
    disclosure_requirements: List[DisclosureRequirement]
    datapoints: List[str]


class ESRSDatapointResponse(BaseModel):
    id: str
    standard: str
    name: str
    type: str
    unit: Optional[str] = None
    description: str


class ESRSStandardListResponse(BaseModel):
    total: int
    standards: List[ESRSStandardResponse]


class ESRSDatapointListResponse(BaseModel):
    total: int
    datapoints: List[ESRSDatapointResponse]


# --- Metrics ---

class MetricCreateRequest(BaseModel):
    datapoint_id: str = Field(..., description="ESRS datapoint identifier (e.g. DP-E1-1)")
    standard_id: str = Field(..., description="ESRS standard identifier (e.g. ESRS_E1)")
    value: str = Field(..., description="Numeric value or text content")
    unit: Optional[str] = Field(None, description="Unit of measurement (tCO2e, m3, EUR, etc.)")
    period_start: Optional[str] = Field(None, description="Start of reporting period (YYYY-MM-DD)")
    period_end: Optional[str] = Field(None, description="End of reporting period (YYYY-MM-DD)")
    source: Optional[str] = Field(None, description="Data source reference")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class MetricResponse(BaseModel):
    id: str
    datapoint_id: str
    standard_id: str
    value: str
    unit: Optional[str] = None
    period_start: Optional[str] = None
    period_end: Optional[str] = None
    source: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime


class MetricListResponse(BaseModel):
    total: int
    metrics: List[MetricResponse]


# --- Reports ---

class ReportDraftRequest(BaseModel):
    title: str = Field(..., description="Report title")
    reporting_period: Optional[str] = Field(None, description="Reporting period label (e.g. FY2025)")
    include_standards: Optional[List[str]] = Field(None, description="Filter by ESRS standard IDs")
    version: Optional[str] = Field(None, description="Report version label")


class ReportResponse(BaseModel):
    id: str
    title: str
    status: str
    reporting_period: Optional[str] = None
    metrics_used: Optional[List[str]] = None
    content: Optional[Dict[str, Any]] = None
    version: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class ReportListResponse(BaseModel):
    total: int
    reports: List[ReportResponse]


# --- Compliance ---

class ComplianceAssessmentRequest(BaseModel):
    standard_ids: Optional[List[str]] = Field(None, description="ESRS standards to assess (all if omitted)")
    reporting_period: Optional[str] = Field(None, description="Reporting period to assess")


class ComplianceCategoryScore(BaseModel):
    category: str
    total_datapoints: int
    completed_datapoints: int
    score_percent: float
    status: str  # compliant, partially_compliant, non_compliant


class ComplianceAssessmentResponse(BaseModel):
    reporting_period: Optional[str] = None
    overall_score: float
    overall_status: str
    total_datapoints: int
    completed_datapoints: int
    categories: List[ComplianceCategoryScore]
    missing_datapoints: List[str]
    recommendations: List[str]
