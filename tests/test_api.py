"""Tests for the SustainaLink CSRD API routes."""

import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health(client):
    resp = await client.get("/api/v1/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "SustainaLink" in data["service"]


@pytest.mark.asyncio
async def test_list_standards(client):
    resp = await client.get("/api/v1/esrs/standards")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 12
    ids = [s["id"] for s in data["standards"]]
    assert "ESRS_E1" in ids
    assert "ESRS_S1" in ids
    assert "ESRS_G1" in ids


@pytest.mark.asyncio
async def test_list_standards_filtered(client):
    resp = await client.get("/api/v1/esrs/standards?category=environmental")
    assert resp.status_code == 200
    data = resp.json()
    assert all(s["category"] == "environmental" for s in data["standards"])


@pytest.mark.asyncio
async def test_get_standard(client):
    resp = await client.get("/api/v1/esrs/standards/ESRS_E1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Climate Change"
    assert len(data["disclosure_requirements"]) > 0


@pytest.mark.asyncio
async def test_get_standard_not_found(client):
    resp = await client.get("/api/v1/esrs/standards/ESRS_XX")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_list_datapoints(client):
    resp = await client.get("/api/v1/esrs/datapoints")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] > 0


@pytest.mark.asyncio
async def test_create_and_list_metric(client):
    # Create
    create_resp = await client.post("/api/v1/metrics", json={
        "datapoint_id": "DP-E1-1",
        "standard_id": "ESRS_E1",
        "value": "12500",
        "unit": "tCO2e",
        "period_start": "2025-01-01",
        "period_end": "2025-12-31",
        "source": "Energy bills and fuel records",
    })
    assert create_resp.status_code == 201
    metric = create_resp.json()
    assert metric["datapoint_id"] == "DP-E1-1"

    # List
    list_resp = await client.get("/api/v1/metrics")
    assert list_resp.status_code == 200
    assert list_resp.json()["total"] >= 1


@pytest.mark.asyncio
async def test_draft_report(client):
    # First ensure we have metrics
    await client.post("/api/v1/metrics", json={
        "datapoint_id": "DP-E1-1",
        "standard_id": "ESRS_E1",
        "value": "12500",
        "unit": "tCO2e",
    })
    await client.post("/api/v1/metrics", json={
        "datapoint_id": "DP-S1-1",
        "standard_id": "ESRS_S1",
        "value": "450",
        "unit": "headcount",
    })

    resp = await client.post("/api/v1/reports/draft", json={
        "title": "CSRD Report FY2025",
        "reporting_period": "FY2025",
        "version": "0.1.0",
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "CSRD Report FY2025"
    assert data["status"] == "draft"
    assert len(data["content"]["sections"]) > 0


@pytest.mark.asyncio
async def test_compliance_assessment(client):
    # Add some metrics first
    await client.post("/api/v1/metrics", json={
        "datapoint_id": "DP-E1-1",
        "standard_id": "ESRS_E1",
        "value": "10000",
        "unit": "tCO2e",
    })

    resp = await client.post("/api/v1/compliance/assess", json={
        "reporting_period": "FY2025",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "overall_score" in data
    assert "overall_status" in data
    assert "categories" in data
    assert "recommendations" in data
