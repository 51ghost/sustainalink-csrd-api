# API Endpoints

**Base URL:** `http://localhost:8000/api/v1`

Interactive documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc) when the server is running.

---

## Health

| Method | Path      | Description     |
| ------ | --------- | --------------- |
| GET    | `/health` | Service health  |

### Response

```json
{
  "status": "ok",
  "version": "0.1.0",
  "service": "SustainaLink CSRD API"
}
```

---

## ESRS Standards

| Method | Path                      | Description                     |
| ------ | ------------------------- | ------------------------------- |
| GET    | `/esrs/standards`         | List all ESRS standards         |
| GET    | `/esrs/standards/{id}`    | Get a specific standard         |
| GET    | `/esrs/datapoints`        | List all data points            |
| GET    | `/esrs/datapoints/{id}`   | Get a specific data point       |

### Query Parameters

- `GET /esrs/standards?category=environmental` — Filter by category: `cross-cutting`, `environmental`, `social`, `governance`
- `GET /esrs/datapoints?standard=ESRS_E1` — Filter by standard ID

---

## Metrics

| Method | Path             | Description              |
| ------ | ---------------- | ------------------------ |
| POST   | `/metrics`       | Record a new metric      |
| GET    | `/metrics`       | List recorded metrics    |
| GET    | `/metrics/{id}`  | Get a specific metric    |

### Create Metric

```json
{
  "datapoint_id": "DP-E1-1",
  "standard_id": "ESRS_E1",
  "value": "12500",
  "unit": "tCO2e",
  "period_start": "2025-01-01",
  "period_end": "2025-12-31",
  "source": "Energy bills",
  "metadata": {}
}
```

### Query Parameters (List)

- `standard_id` — Filter by ESRS standard
- `datapoint_id` — Filter by data point
- `limit` — Default 50
- `offset` — Default 0

---

## Reports

| Method | Path              | Description                  |
| ------ | ----------------- | ---------------------------- |
| POST   | `/reports/draft`  | Generate a draft CSRD report |
| GET    | `/reports`        | List all reports             |
| GET    | `/reports/{id}`   | Get a specific report        |

### Draft Report

```json
{
  "title": "CSRD Report FY2025",
  "reporting_period": "FY2025",
  "include_standards": ["ESRS_E1", "ESRS_S1"],
  "version": "0.1.0"
}
```

---

## Compliance

| Method | Path                    | Description                    |
| ------ | ----------------------- | ------------------------------ |
| POST   | `/compliance/assess`    | Run compliance assessment      |

### Assessment

```json
{
  "standard_ids": ["ESRS_E1"],
  "reporting_period": "FY2025"
}
```

Returns:
- `overall_score` — percentage of data points completed
- `overall_status` — compliant / partially_compliant / non_compliant
- `categories` — per-category breakdown
- `missing_datapoints` — list of data points not yet recorded
- `recommendations` — actionable suggestions
