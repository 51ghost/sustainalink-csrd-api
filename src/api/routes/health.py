"""Health check endpoint."""

from fastapi import APIRouter

from config.settings import settings
from src.schemas.responses import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Return service health status."""
    return HealthResponse(
        status="ok",
        version=settings.app_version,
        service=settings.app_name,
    )
