"""Pytest configuration for SustainaLink CSRD API tests."""

import pytest
from src.database.session import init_db
from config.settings import settings


@pytest.fixture(autouse=True)
async def _ensure_db():
    """Ensure database tables exist before each test."""
    await init_db()
    yield
