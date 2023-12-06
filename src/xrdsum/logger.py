"""Application level logger for xrdsum"""
from __future__ import annotations

import logging

from fasthep_logging import TIMING, TRACE
from fasthep_logging import get_logger as flogger
from fasthep_logging._logging import FASTHEPLogger

APP_LOGGER_NAME = "xrdsum"


def get_logger(
    logger_name: str = APP_LOGGER_NAME,
    default_level: int = logging.INFO,
    log_file: str | None = None,
) -> FASTHEPLogger:
    flogger(logger_name, default_level, log_file)
    return FASTHEPLogger(logger_name, default_level)


__all__ = ["APP_LOGGER_NAME", "get_logger", "TIMING", "TRACE"]
