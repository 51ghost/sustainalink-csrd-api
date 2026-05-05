# SustainaLink CSRD API

A **FastAPI**-based REST API for **CSRD (Corporate Sustainability Reporting Directive)** compliance and **ESRS (European Sustainability Reporting Standards)** management — built by SustainaLink.

> **SustainaLink** brings together students and companies to collaborate on impactful sustainability projects. This API provides technical infrastructure for the CSRD reporting ecosystem.

---

## Features

- ✅ **ESRS Standards Registry** — Complete taxonomy of all 12 ESRS standards with data points, disclosure requirements, and application guidance
- ✅ **Materiality Assessment** — Double materiality analysis workflow (impact + financial materiality)
- ✅ **Metrics Engine** — Structured sustainability metrics aligned to ESRS data points with units, sources, and validation rules
- ✅ **Report Generation** — Draft CSRD-compliant sustainability reports from collected metrics
- ✅ **Compliance Scoring** — Gap analysis and readiness assessment against CSRD requirements
- ✅ **OpenAPI Documentation** — Auto-generated interactive API docs at `/docs`

## Quick Start

```bash
# Clone the repo
git clone https://github.com/sustainalink/csrd-api.git
cd csrd-api

# Install dependencies
pip install -e ".[dev]"

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn src.main:app --reload --port 8000

# Open API docs
open http://localhost:8000/docs
```

## Docker

```bash
docker compose up --build
```

## API Overview

| Method | Endpoint                          | Description                              |
| ------ | --------------------------------- | ---------------------------------------- |
| GET    | `/api/v1/health`                  | Health check                             |
| GET    | `/api/v1/esrs/standards`          | List all ESRS standards                  |
| GET    | `/api/v1/esrs/standards/{id}`     | Get a specific ESRS standard             |
| GET    | `/api/v1/esrs/datapoints`         | List data points with optional filtering |
| POST   | `/api/v1/metrics`                 | Create/record a sustainability metric    |
| GET    | `/api/v1/metrics`                 | List recorded metrics                    |
| GET    | `/api/v1/metrics/{id}`            | Get metric details                       |
| POST   | `/api/v1/reports/draft`           | Generate a draft CSRD report             |
| GET    | `/api/v1/reports`                 | List generated reports                   |
| GET    | `/api/v1/reports/{id}`            | Get report details                       |
| POST   | `/api/v1/compliance/assess`       | Run compliance assessment                |

## Project Structure

```
src/
├── main.py              # FastAPI application entrypoint
├── api/
│   ├── routes/          # Route handlers (health, esrs, metrics, reports, compliance)
│   ├── dependencies.py  # FastAPI dependency injection
│   └── middleware.py    # Custom middleware (CORS, timing, etc.)
├── models/              # ESRS definitions & domain models
├── services/            # Business logic layer
├── schemas/             # Pydantic request/response schemas
└── database/            # SQLAlchemy models & session management
config/
├── settings.py          # Application settings via pydantic-settings
└── esrs_standards.json  # ESRS standard definitions data
docs/                    # Extended documentation
tests/                   # Test suite
examples/                # Usage examples
```

## ESRS Standards Covered

| Standard | Topic                                      |
| -------- | ------------------------------------------ |
| ESRS 1   | General Requirements                       |
| ESRS 2   | General Disclosures                        |
| ESRS E1  | Climate Change                             |
| ESRS E2  | Pollution                                  |
| ESRS E3  | Water & Marine Resources                   |
| ESRS E4  | Biodiversity & Ecosystems                  |
| ESRS E5  | Resource Use & Circular Economy            |
| ESRS S1  | Own Workforce                              |
| ESRS S2  | Workers in the Value Chain                 |
| ESRS S3  | Affected Communities                       |
| ESRS S4  | Consumers & End-Users                      |
| ESRS G1  | Business Conduct                           |

## License

MIT — See [LICENSE](LICENSE)


---
Trigger: 1778001288
