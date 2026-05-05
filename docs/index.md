# SustainaLink CSRD API Documentation

Welcome to the documentation for the **SustainaLink CSRD API** — a FastAPI-based REST API for managing CSRD (Corporate Sustainability Reporting Directive) compliance and ESRS (European Sustainability Reporting Standards) reporting.

## Table of Contents

- [Getting Started](#getting-started)
- [Core Concepts](#core-concepts)
- [API Endpoints](api/endpoints.md)
- [ESRS Standards Reference](esrs/standards.md)

## Getting Started

### Prerequisites

- Python 3.11+
- pip or uv

### Installation

```bash
pip install -e ".[dev]"
```

### Configuration

Copy the environment template and adjust as needed:

```bash
cp .env.example .env
```

### Running

```bash
uvicorn src.main:app --reload --port 8000
```

### Docker

```bash
docker compose up --build
```

## Core Concepts

### CSRD

The **Corporate Sustainability Reporting Directive (CSRD)** is an EU regulation requiring large and listed companies to disclose sustainability information. It entered into force in January 2023, with phased implementation from 2024 onward.

### ESRS

The **European Sustainability Reporting Standards (ESRS)** are the detailed standards that operationalize the CSRD. There are 12 standards covering environmental, social, and governance topics.

### Double Materiality

CSRD requires a **double materiality** assessment:
- **Impact materiality**: how the company affects people and the environment
- **Financial materiality**: how sustainability risks and opportunities affect the company

### Data Points

Each ESRS standard contains specific **data points** — the individual metrics and disclosures required for compliance. This API provides a registry of all data points and allows you to record values for them.

## License

MIT
