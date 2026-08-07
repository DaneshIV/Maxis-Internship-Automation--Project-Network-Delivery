"""
main.py
-------
Entry point for the CMS Automation pipeline.
Runs the full flow: Excel parse → AI predict → CMS insert.
"""

from src.utils.logger import get_logger
from src.utils.config_loader import load_config, validate_config, get_settings

logger = get_logger(__name__)


def run():
    logger.info("=" * 60)
    logger.info("CMS Automation Pipeline — Starting")
    logger.info("=" * 60)

    # 1. Load and validate config
    logger.info("Loading field mapping config...")
    config = load_config()
    settings = get_settings(config)

    warnings = validate_config(config)
    if warnings:
        logger.warning(f"{len(warnings)} placeholder(s) still in config — CMS access needed to resolve.")
        for w in warnings:
            logger.warning(w)

    # 2. Parse Excel
    # TODO: uncomment once excel_parser.py is ready
    # from src.parser.excel_parser import ExcelParser
    # parser = ExcelParser(config)
    # records = parser.parse("data/raw/your_file.xlsx")
    # logger.info(f"Parsed {len(records)} records from Excel.")

    # 3. AI Prediction
    # TODO: uncomment once predict.py and trained model are ready
    # from src.ai.predict import Predictor
    # predictor = Predictor()
    # records = predictor.fill_missing(records)

    # 4. CMS Automation
    # TODO: uncomment once cms_automation.py and CMS access are ready
    # from src.automation.cms_automation import CMSAutomation
    # cms = CMSAutomation(config)
    # cms.run(records)

    logger.info("Pipeline complete.")


if __name__ == "__main__":
    run()
