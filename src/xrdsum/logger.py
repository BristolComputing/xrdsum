"""Application level logger for xrdsum"""
from __future__ import annotations

from fasthep_logging import TIMING, TRACE, get_logger

APP_LOGGER_NAME = "xrdsum"

__all__ = [APP_LOGGER_NAME, get_logger, TIMING, TRACE]
