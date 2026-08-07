"""
logger.py
---------
Shared logging module for the CMS Automation project.
All modules call get_logger(__name__) — never configure logging directly.
"""

import logging
import os
from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = LOG_DIR / f"cms_automation_{datetime.now().strftime('%Y%m%d')}.log"

_configured = False


def _configure():
    global _configured
    if _configured:
        return

    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL, logging.INFO),
        format=fmt,
        datefmt=datefmt,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
    )
    _configured = True


def get_logger(name: str) -> logging.Logger:
    """Return a named logger. Call with get_logger(__name__) in every module."""
    _configure()
    return logging.getLogger(name)
