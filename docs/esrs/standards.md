# ESRS Standards Reference

The European Sustainability Reporting Standards (ESRS) are the detailed standards adopted by the European Commission under the CSRD. There are 12 standards organized into four categories.

## Categories

### Cross-Cutting Standards (ESRS 1 & 2)

These apply to all companies and define general reporting principles.

| Standard | Name                  | Key Topics                                         |
| -------- | --------------------- | -------------------------------------------------- |
| ESRS 1   | General Requirements  | Basis of preparation, materiality, value chain     |
| ESRS 2   | General Disclosures   | Strategy, governance, stakeholder engagement, IROs |

### Environmental Standards (ESRS E1–E5)

| Standard | Name                            | Key Topics                                              |
| -------- | ------------------------------- | ------------------------------------------------------- |
| ESRS E1  | Climate Change                  | GHG emissions, transition plans, climate risks          |
| ESRS E2  | Pollution                       | Air/water/soil pollution, substances of concern         |
| ESRS E3  | Water & Marine Resources        | Water consumption, withdrawals, marine impacts          |
| ESRS E4  | Biodiversity & Ecosystems       | Land use, deforestation, ecosystem restoration          |
| ESRS E5  | Resource Use & Circular Economy | Resource inflows/outflows, waste, circularity           |

### Social Standards (ESRS S1–S4)

| Standard | Name                         | Key Topics                                            |
| -------- | ---------------------------- | ----------------------------------------------------- |
| ESRS S1  | Own Workforce                | Working conditions, diversity, health & safety        |
| ESRS S2  | Workers in the Value Chain   | Supply chain labor conditions, human rights           |
| ESRS S3  | Affected Communities         | Community impacts, indigenous rights                  |
| ESRS S4  | Consumers & End-Users        | Consumer safety, data privacy, product labeling       |

### Governance Standard (ESRS G1)

| Standard | Name             | Key Topics                                        |
| -------- | ---------------- | ------------------------------------------------- |
| ESRS G1  | Business Conduct | Anti-corruption, supplier relations, lobbying     |

---

## Data Points

Each standard contains specific **data points** that companies must report on. The API provides a structured registry of all data points with metadata including:

- **ID** — Unique identifier (e.g., `DP-E1-1`)
- **Type** — `numeric` or `text`
- **Unit** — Unit of measurement (e.g., `tCO2e`, `m3`, `EUR`)
- **Description** — What the data point represents

### Example Data Points

| ID        | Standard | Name                 | Type    | Unit      |
| --------- | -------- | -------------------- | ------- | --------- |
| DP-E1-1   | ESRS E1  | GHG Scope 1          | numeric | tCO2e     |
| DP-E1-2   | ESRS E1  | GHG Scope 2          | numeric | tCO2e     |
| DP-S1-1   | ESRS S1  | Employee count       | numeric | headcount |
| DP-S1-3   | ESRS S1  | Gender diversity     | numeric | percent   |
| DP-G1-2   | ESRS G1  | Payment practices    | numeric | days      |

---

## Materiality Assessment

Under CSRD, companies must perform a **double materiality assessment**:

1. **Impact Materiality** — Identify actual and potential positive/negative impacts on people and the environment
2. **Financial Materiality** — Identify sustainability-related risks and opportunities that affect financial performance

Data points that are deemed material must be reported. The API can help track which data points have been deemed material and which values have been recorded.

---

## Resources

- [Official ESRS Delegated Act](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13765-European-sustainability-reporting-standards_en)
- [EFRAG ESRS Resource Page](https://www.efrag.org/lab6)
- [CSRD Text (Official Journal)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2464)
