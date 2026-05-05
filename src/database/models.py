"""SQLAlchemy ORM models for the SustainaLink CSRD API."""

import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, Text, DateTime, JSON
from src.database.session import Base


def _uuid() -> str:
    return str(uuid.uuid4())


def _now() -> datetime:
    return datetime.now(timezone.utc)


class MetricModel(Base):
    __tablename__ = "metrics"

    id = Column(String, primary_key=True, default=_uuid)
    datapoint_id = Column(String, nullable=False, index=True)
    standard_id = Column(String, nullable=False, index=True)
    value = Column(Text, nullable=False)
    unit = Column(String, nullable=True)
    period_start = Column(String, nullable=True)
    period_end = Column(String, nullable=True)
    source = Column(String, nullable=True)
    metadata_ = Column("metadata", JSON, nullable=True)
    created_at = Column(DateTime, default=_now)
    updated_at = Column(DateTime, default=_now, onupdate=_now)


class ReportModel(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True, default=_uuid)
    title = Column(String, nullable=False)
    status = Column(String, default="draft")
    reporting_period = Column(String, nullable=True)
    metrics_used = Column(JSON, nullable=True)
    content = Column(JSON, nullable=True)
    version = Column(String, nullable=True)
    created_at = Column(DateTime, default=_now)
    updated_at = Column(DateTime, default=_now, onupdate=_now)
