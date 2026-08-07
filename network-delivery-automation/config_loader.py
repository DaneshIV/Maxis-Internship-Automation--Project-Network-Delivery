"""
config_loader.py
----------------
Loads and validates the field mapping YAML config at runtime.
All other modules import from here — never read the YAML directly.
"""

import yaml
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = Path(__file__).parent.parent / "config" / "field_mapping.yaml"


def load_config(path: Path = CONFIG_PATH) -> dict:
    """Load the full field mapping config from YAML."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_excel_to_cms_map(config: dict) -> dict:
    """
    Return a flat dict: { excel_column_name: cms_field_name }
    Only includes entries with status != 'skip'.
    """
    mapping = {}
    for entry in config.get("excel_to_cms", []):
        if entry.get("status") == "skip":
            continue
        mapping[entry["excel_column"]] = {
            "cms_field":    entry["cms_field"],
            "data_type":    entry.get("data_type", "string"),
            "required":     entry.get("required", False),
            "date_format":  entry.get("date_format"),
            "status":       entry.get("status"),
            "notes":        entry.get("notes", ""),
        }
    return mapping


def get_mandatory_columns(config: dict) -> list:
    """Return the list of mandatory Excel columns that must not be empty."""
    return config.get("settings", {}).get("mandatory_columns", [])


def get_cms_only_fields(config: dict) -> list:
    """Return fields that exist in CMS but not in Excel."""
    return config.get("cms_only_fields", [])


def get_prediction_target(config: dict) -> dict | None:
    """Return the CMS field marked for AI prediction, if any."""
    for field in config.get("cms_only_fields", []):
        if field.get("status") == "predict":
            return field
    return None


def get_settings(config: dict) -> dict:
    """Return global settings block."""
    return config.get("settings", {})


def validate_config(config: dict) -> list:
    """
    Run basic validation on the loaded config.
    Returns a list of warning strings — empty list means all good.
    """
    warnings = []
    for entry in config.get("excel_to_cms", []):
        if "TODO" in str(entry.get("cms_field", "")):
            warnings.append(
                f"[PLACEHOLDER] '{entry['excel_column']}' → cms_field not yet confirmed."
            )
    for field in config.get("cms_only_fields", []):
        if "TODO" in str(field.get("cms_field", "")):
            warnings.append(
                f"[PLACEHOLDER] CMS-only field not yet identified: {field['cms_field']}"
            )
    return warnings


# ── Quick self-test when run directly ────────────────────────────────────────
if __name__ == "__main__":
    cfg = load_config()

    print("=" * 60)
    print("FIELD MAPPING SUMMARY")
    print("=" * 60)

    mapping = get_excel_to_cms_map(cfg)
    for excel_col, details in mapping.items():
        status_tag = f"[{details['status'].upper()}]"
        print(f"  {status_tag:<15} {excel_col:<45} → {details['cms_field']}")

    print()
    mandatory = get_mandatory_columns(cfg)
    print(f"Mandatory columns : {mandatory}")

    predict = get_prediction_target(cfg)
    print(f"AI predict target : {predict}")

    print()
    print("CONFIG WARNINGS")
    print("-" * 60)
    warnings = validate_config(cfg)
    if warnings:
        for w in warnings:
            print(f"  ⚠  {w}")
    else:
        print("  ✓ No warnings — all fields confirmed.")

    print("=" * 60)