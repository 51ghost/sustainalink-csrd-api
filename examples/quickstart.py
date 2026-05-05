"""Quickstart example — demonstrates basic usage of the SustainaLink CSRD API."""

import httpx
import asyncio

BASE_URL = "http://localhost:8000/api/v1"


async def example():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=30) as client:
        # 1. Health check
        resp = await client.get("/health")
        print(f"✅ Health: {resp.json()}")

        # 2. List ESRS standards
        resp = await client.get("/esrs/standards?category=environmental")
        print(f"✅ Environmental standards: {resp.json()['total']} found")

        # 3. Record metrics (GHG emissions — ESRS E1)
        metrics_data = [
            {
                "datapoint_id": "DP-E1-1",
                "standard_id": "ESRS_E1",
                "value": "12500",
                "unit": "tCO2e",
                "period_start": "2025-01-01",
                "period_end": "2025-12-31",
                "source": "Energy bills",
            },
            {
                "datapoint_id": "DP-E1-2",
                "standard_id": "ESRS_E1",
                "value": "4800",
                "unit": "tCO2e",
                "period_start": "2025-01-01",
                "period_end": "2025-12-31",
                "source": "Electricity provider records",
            },
            {
                "datapoint_id": "DP-S1-1",
                "standard_id": "ESRS_S1",
                "value": "450",
                "unit": "headcount",
                "period_start": "2025-01-01",
                "period_end": "2025-12-31",
            },
        ]
        for m in metrics_data:
            resp = await client.post("/metrics", json=m)
            print(f"✅ Created metric: {resp.json()['id'][:8]}... ({m['datapoint_id']})")

        # 4. Generate draft CSRD report
        resp = await client.post("/reports/draft", json={
            "title": "SustainaLink CSRD Report FY2025",
            "reporting_period": "FY2025",
        })
        report = resp.json()
        print(f"✅ Draft report: {report['id'][:8]}... ({report['status']})")
        print(f"   Sections: {len(report['content']['sections'])}")

        # 5. Run compliance assessment
        resp = await client.post("/compliance/assess", json={
            "reporting_period": "FY2025",
        })
        assessment = resp.json()
        print(f"✅ Compliance: {assessment['overall_score']}% — {assessment['overall_status']}")
        print(f"   Completed: {assessment['completed_datapoints']}/{assessment['total_datapoints']}")
        for rec in assessment["recommendations"]:
            print(f"   → {rec}")


if __name__ == "__main__":
    asyncio.run(example())
