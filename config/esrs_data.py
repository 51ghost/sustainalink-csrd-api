"""
ESRS (European Sustainability Reporting Standards) — complete taxonomy.

This file defines the 12 ESRS standards with their metadata,
disclosure requirements, and data point mappings.

Based on the official ESRS adopted by the European Commission
under the CSRD (Corporate Sustainability Reporting Directive).
"""

ESRS_STANDARDS = [
    {
        "id": "ESRS_1",
        "name": "General Requirements",
        "category": "cross-cutting",
        "description": "General principles for sustainability reporting, including materiality assessment, value chain reporting, and preparation basis.",
        "disclosure_requirements": [
            {"id": "ESRS_1_1", "title": "Basis of preparation", "description": "General basis for preparing sustainability statements."},
            {"id": "ESRS_1_2", "title": "Materiality assessment", "description": "Process for determining material impacts, risks, and opportunities."},
            {"id": "ESRS_1_3", "title": "Value chain", "description": "Scope of value chain reporting requirements."},
        ],
        "datapoints": ["DP-1-1", "DP-1-2", "DP-1-3"],
    },
    {
        "id": "ESRS_2",
        "name": "General Disclosures",
        "category": "cross-cutting",
        "description": "Mandatory disclosures applicable to all companies, including strategy, governance, and materiality analysis.",
        "disclosure_requirements": [
            {"id": "ESRS_2_1", "title": "Strategy, business model and value chain", "description": "Description of strategy, business model and value chain in relation to sustainability."},
            {"id": "ESRS_2_2", "title": "Interests and views of stakeholders", "description": "Stakeholder engagement processes and outcomes."},
            {"id": "ESRS_2_3", "title": "Material impacts, risks and opportunities", "description": "Process to identify and assess material IROs."},
        ],
        "datapoints": ["DP-2-1", "DP-2-2", "DP-2-3"],
    },
    {
        "id": "ESRS_E1",
        "name": "Climate Change",
        "category": "environmental",
        "description": "Climate-related disclosures including GHG emissions, climate transition plans, and physical/transition risk management.",
        "disclosure_requirements": [
            {"id": "ESRS_E1_1", "title": "Climate transition plan", "description": "Company's plan for transitioning to a sustainable economy and limiting global warming to 1.5°C."},
            {"id": "ESRS_E1_2", "title": "GHG emissions", "description": "Scope 1, 2, and 3 greenhouse gas emissions."},
            {"id": "ESRS_E1_3", "title": "Climate risk assessment", "description": "Physical and transition risks from climate change."},
        ],
        "datapoints": ["DP-E1-1", "DP-E1-2", "DP-E1-3", "DP-E1-4"],
    },
    {
        "id": "ESRS_E2",
        "name": "Pollution",
        "category": "environmental",
        "description": "Disclosures on air, water, and soil pollution, including substances of concern and microplastics.",
        "disclosure_requirements": [
            {"id": "ESRS_E2_1", "title": "Pollution management", "description": "Policies and actions to prevent and control pollution."},
            {"id": "ESRS_E2_2", "title": "Pollution metrics", "description": "Measurement of emissions to air, water, and soil."},
        ],
        "datapoints": ["DP-E2-1", "DP-E2-2", "DP-E2-3"],
    },
    {
        "id": "ESRS_E3",
        "name": "Water and Marine Resources",
        "category": "environmental",
        "description": "Disclosures on water consumption, water withdrawals, and impacts on marine ecosystems.",
        "disclosure_requirements": [
            {"id": "ESRS_E3_1", "title": "Water management", "description": "Policies and actions related to water resources."},
            {"id": "ESRS_E3_2", "title": "Water metrics", "description": "Water consumption, withdrawal, and discharge metrics."},
        ],
        "datapoints": ["DP-E3-1", "DP-E3-2"],
    },
    {
        "id": "ESRS_E4",
        "name": "Biodiversity and Ecosystems",
        "category": "environmental",
        "description": "Disclosures on impacts on biodiversity and ecosystems, including land use and deforestation.",
        "disclosure_requirements": [
            {"id": "ESRS_E4_1", "title": "Biodiversity policies", "description": "Transition plan and policies for biodiversity."},
            {"id": "ESRS_E4_2", "title": "Biodiversity metrics", "description": "Metrics related to biodiversity and ecosystem impacts."},
        ],
        "datapoints": ["DP-E4-1", "DP-E4-2"],
    },
    {
        "id": "ESRS_E5",
        "name": "Resource Use and Circular Economy",
        "category": "environmental",
        "description": "Disclosures on resource use, waste management, and circular economy practices.",
        "disclosure_requirements": [
            {"id": "ESRS_E5_1", "title": "Circular economy policies", "description": "Policies and actions for transitioning to circular economy."},
            {"id": "ESRS_E5_2", "title": "Resource flows", "description": "Resource inflows, outflows, and waste metrics."},
        ],
        "datapoints": ["DP-E5-1", "DP-E5-2", "DP-E5-3"],
    },
    {
        "id": "ESRS_S1",
        "name": "Own Workforce",
        "category": "social",
        "description": "Disclosures on company's own workforce including working conditions, diversity, and health & safety.",
        "disclosure_requirements": [
            {"id": "ESRS_S1_1", "title": "Workforce characteristics", "description": "Characteristics of the company's own employees and non-employees."},
            {"id": "ESRS_S1_2", "title": "Working conditions", "description": "Working time, health and safety, remuneration, and social dialogue."},
            {"id": "ESRS_S1_3", "title": "Diversity and inclusion", "description": "Diversity metrics and equal opportunity policies."},
        ],
        "datapoints": ["DP-S1-1", "DP-S1-2", "DP-S1-3", "DP-S1-4"],
    },
    {
        "id": "ESRS_S2",
        "name": "Workers in the Value Chain",
        "category": "social",
        "description": "Disclosures on workers in the upstream and downstream value chain.",
        "disclosure_requirements": [
            {"id": "ESRS_S2_1", "title": "Value chain workforce assessment", "description": "Assessment of working conditions in the value chain."},
            {"id": "ESRS_S2_2", "title": "Value chain engagement", "description": "Processes for engaging with value chain workers."},
        ],
        "datapoints": ["DP-S2-1", "DP-S2-2"],
    },
    {
        "id": "ESRS_S3",
        "name": "Affected Communities",
        "category": "social",
        "description": "Disclosures on impacts on communities affected by company operations.",
        "disclosure_requirements": [
            {"id": "ESRS_S3_1", "title": "Community impacts", "description": "Economic, social and cultural impacts on communities."},
            {"id": "ESRS_S3_2", "title": "Indigenous rights", "description": "Respect for the rights of indigenous peoples."},
        ],
        "datapoints": ["DP-S3-1", "DP-S3-2"],
    },
    {
        "id": "ESRS_S4",
        "name": "Consumers and End-Users",
        "category": "social",
        "description": "Disclosures on impacts on consumers and end-users of products and services.",
        "disclosure_requirements": [
            {"id": "ESRS_S4_1", "title": "Consumer protection", "description": "Policies and actions for consumer health, safety, and privacy."},
            {"id": "ESRS_S4_2", "title": "Consumer engagement", "description": "Processes for engaging with consumers and end-users."},
        ],
        "datapoints": ["DP-S4-1", "DP-S4-2"],
    },
    {
        "id": "ESRS_G1",
        "name": "Business Conduct",
        "category": "governance",
        "description": "Disclosures on business ethics, anti-corruption, supplier relationships, and political engagement.",
        "disclosure_requirements": [
            {"id": "ESRS_G1_1", "title": "Business ethics and anti-corruption", "description": "Policies against corruption and bribery."},
            {"id": "ESRS_G1_2", "title": "Supplier relationship management", "description": "Payment practices and supplier engagement."},
            {"id": "ESRS_G1_3", "title": "Political engagement", "description": "Lobbying activities and political contributions."},
        ],
        "datapoints": ["DP-G1-1", "DP-G1-2", "DP-G1-3"],
    },
]

DATAPOINTS = {
    "DP-1-1": {"standard": "ESRS_1", "name": "Reporting scope", "type": "text", "unit": None, "description": "Scope of entities included in sustainability statement."},
    "DP-1-2": {"standard": "ESRS_1", "name": "Materiality process", "type": "text", "unit": None, "description": "Description of materiality assessment process."},
    "DP-1-3": {"standard": "ESRS_1", "name": "Value chain scope", "type": "text", "unit": None, "description": "Description of value chain boundaries."},
    "DP-2-1": {"standard": "ESRS_2", "name": "Business model description", "type": "text", "unit": None, "description": "Description of business model and strategy."},
    "DP-2-2": {"standard": "ESRS_2", "name": "Stakeholder engagement", "type": "text", "unit": None, "description": "Description of stakeholder engagement processes."},
    "DP-2-3": {"standard": "ESRS_2", "name": "IRO assessment", "type": "text", "unit": None, "description": "Assessment of material impacts, risks and opportunities."},
    "DP-E1-1": {"standard": "ESRS_E1", "name": "GHG Scope 1", "type": "numeric", "unit": "tCO2e", "description": "Direct greenhouse gas emissions (Scope 1)."},
    "DP-E1-2": {"standard": "ESRS_E1", "name": "GHG Scope 2", "type": "numeric", "unit": "tCO2e", "description": "Indirect greenhouse gas emissions from energy (Scope 2)."},
    "DP-E1-3": {"standard": "ESRS_E1", "name": "GHG Scope 3", "type": "numeric", "unit": "tCO2e", "description": "Value chain greenhouse gas emissions (Scope 3)."},
    "DP-E1-4": {"standard": "ESRS_E1", "name": "Climate transition plan", "type": "text", "unit": None, "description": "Climate transition plan aligned with 1.5°C pathway."},
    "DP-E2-1": {"standard": "ESRS_E2", "name": "Air emissions", "type": "numeric", "unit": "kg", "description": "Emissions of pollutants to air."},
    "DP-E2-2": {"standard": "ESRS_E2", "name": "Water pollution", "type": "numeric", "unit": "kg", "description": "Emissions of pollutants to water."},
    "DP-E2-3": {"standard": "ESRS_E2", "name": "Soil pollution", "type": "numeric", "unit": "kg", "description": "Emissions of pollutants to soil."},
    "DP-E3-1": {"standard": "ESRS_E3", "name": "Water consumption", "type": "numeric", "unit": "m3", "description": "Total water consumption."},
    "DP-E3-2": {"standard": "ESRS_E3", "name": "Water withdrawals", "type": "numeric", "unit": "m3", "description": "Total water withdrawals by source."},
    "DP-E4-1": {"standard": "ESRS_E4", "name": "Land use impact", "type": "numeric", "unit": "ha", "description": "Land use change and biodiversity impact."},
    "DP-E4-2": {"standard": "ESRS_E4", "name": "Biodiversity policies", "type": "text", "unit": None, "description": "Biodiversity protection policies and actions."},
    "DP-E5-1": {"standard": "ESRS_E5", "name": "Resource inflows", "type": "numeric", "unit": "t", "description": "Material resource inflows by type."},
    "DP-E5-2": {"standard": "ESRS_E5", "name": "Waste generation", "type": "numeric", "unit": "t", "description": "Total waste generated by type and treatment."},
    "DP-E5-3": {"standard": "ESRS_E5", "name": "Circular economy actions", "type": "text", "unit": None, "description": "Circular economy practices and outcomes."},
    "DP-S1-1": {"standard": "ESRS_S1", "name": "Employee count", "type": "numeric", "unit": "headcount", "description": "Total number of employees."},
    "DP-S1-2": {"standard": "ESRS_S1", "name": "Turnover rate", "type": "numeric", "unit": "percent", "description": "Employee turnover rate."},
    "DP-S1-3": {"standard": "ESRS_S1", "name": "Gender diversity", "type": "numeric", "unit": "percent", "description": "Gender distribution at top management."},
    "DP-S1-4": {"standard": "ESRS_S1", "name": "Health & safety", "type": "numeric", "unit": "rate", "description": "Work-related injury/accident rate."},
    "DP-S2-1": {"standard": "ESRS_S2", "name": "Value chain assessment", "type": "text", "unit": None, "description": "Assessment of value chain working conditions."},
    "DP-S2-2": {"standard": "ESRS_S2", "name": "Supply chain engagement", "type": "text", "unit": None, "description": "Supplier engagement on human rights."},
    "DP-S3-1": {"standard": "ESRS_S3", "name": "Community impact assessment", "type": "text", "unit": None, "description": "Impact on local communities."},
    "DP-S3-2": {"standard": "ESRS_S3", "name": "Indigenous rights", "type": "text", "unit": None, "description": "Indigenous peoples' rights due diligence."},
    "DP-S4-1": {"standard": "ESRS_S4", "name": "Consumer safety", "type": "text", "unit": None, "description": "Consumer health and safety practices."},
    "DP-S4-2": {"standard": "ESRS_S4", "name": "Data privacy", "type": "text", "unit": None, "description": "Data privacy and protection practices."},
    "DP-G1-1": {"standard": "ESRS_G1", "name": "Anti-corruption", "type": "text", "unit": None, "description": "Anti-corruption and anti-bribery policies."},
    "DP-G1-2": {"standard": "ESRS_G1", "name": "Payment practices", "type": "numeric", "unit": "days", "description": "Average payment terms to suppliers."},
    "DP-G1-3": {"standard": "ESRS_G1", "name": "Political spending", "type": "numeric", "unit": "EUR", "description": "Political contributions and lobbying expenditures."},
}
