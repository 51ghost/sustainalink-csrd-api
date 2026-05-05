"""Reporting service — assembles CSRD sustainability report content from metrics."""

from typing import Any, Dict, List

from config.esrs_data import ESRS_STANDARDS, DATAPOINTS


def generate_report_content(metrics: List[Any], title: str) -> Dict[str, Any]:
    """Generate structured CSRD report content from a list of MetricModel records.

    Organizes metrics by ESRS standard, producing a hierarchical report structure
    suitable for downstream rendering or export.
    """
    # Group metrics by standard_id
    by_standard: Dict[str, list] = {}
    for m in metrics:
        by_standard.setdefault(m.standard_id, []).append(m)

    sections = []
    for standard_def in ESRS_STANDARDS:
        std_id = standard_def["id"]
        if std_id not in by_standard:
            continue

        std_metrics = by_standard[std_id]
        datapoint_sections = []
        for m in std_metrics:
            dp_info = DATAPOINTS.get(m.datapoint_id, {})
            datapoint_sections.append({
                "datapoint_id": m.datapoint_id,
                "datapoint_name": dp_info.get("name", m.datapoint_id),
                "value": m.value,
                "unit": m.unit or dp_info.get("unit"),
                "description": dp_info.get("description", ""),
                "source": m.source,
                "period": f"{m.period_start or 'N/A'} to {m.period_end or 'N/A'}",
            })

        sections.append({
            "standard_id": std_id,
            "standard_name": standard_def["name"],
            "category": standard_def["category"],
            "description": standard_def["description"],
            "datapoints": datapoint_sections,
        })

    return {
        "title": title,
        "report_type": "CSRD Sustainability Statement (Draft)",
        "style": "ESRS-structured",
        "sections": sections,
    }
