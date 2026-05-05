# SustainaLink CSRD API — Application Entrypoint

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from src.api.routes import health, esrs, metrics, reports, compliance
from src.database.session import engine, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: initialize database on startup."""
    await init_db()
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "REST API for CSRD (Corporate Sustainability Reporting Directive) "
        "compliance and ESRS standards management. Built by SustainaLink."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(health.router, prefix=settings.api_prefix, tags=["Health"])
app.include_router(esrs.router, prefix=settings.api_prefix, tags=["ESRS"])
app.include_router(metrics.router, prefix=settings.api_prefix, tags=["Metrics"])
app.include_router(reports.router, prefix=settings.api_prefix, tags=["Reports"])
app.include_router(compliance.router, prefix=settings.api_prefix, tags=["Compliance"])
