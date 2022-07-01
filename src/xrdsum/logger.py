from __future__ import annotations

import logging
from typing import Any

from rich.logging import RichHandler

APP_LOGGER_NAME = "xrdsum"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TIME_FORMAT = "%H:%M:%S"
TRACE = 5


def trace(
    self: logging.Logger, message: str, *args: list[Any], **kws: dict[str, Any]
) -> None:
    if self.isEnabledFor(TRACE):
        self._log(TRACE, message, args, **kws)  # type: ignore[arg-type]


class LevelFormatter(logging.Formatter):
    """
    From https://stackoverflow.com/a/28636024/362457
    """

    def __init__(self, fmt: str, datefmt: str, level_fmts: dict[int, str]):
        self._level_formatters = {}
        for level, format in level_fmts.items():
            # Could optionally support level names too
            self._level_formatters[level] = logging.Formatter(
                fmt=format, datefmt=datefmt
            )
        # self._fmt will be the default format
        super().__init__(fmt=fmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        if record.levelno in self._level_formatters:
            return self._level_formatters[record.levelno].format(record)

        return super().format(record)


# add TRACE log level and function to logger
logging.addLevelName(TRACE, "TRACE")
logging.TRACE = TRACE  # type: ignore[attr-defined]

console_formatter = LevelFormatter(
    fmt="%(asctime)s [%(name)s]  %(levelname)s: %(message)s",
    datefmt=f"[{DEFAULT_DATE_FORMAT} {DEFAULT_TIME_FORMAT}]",
    level_fmts={
        logging.INFO: "%(message)s",
        logging.WARNING: "[bold dark_orange]%(levelname)s[/]: %(message)s",
        logging.ERROR: "[bold red]%(levelname)s[/]: %(message)s",
        logging.DEBUG: "[bold hot_pink]%(levelname)s[/]: %(message)s",
        logging.TRACE: "[bold hot_pink]%(levelname)s[/]: %(message)s",  # type: ignore[attr-defined]
        logging.CRITICAL: "[bold blink bright_red]%(levelname)s[/]: %(message)s",
    },
)
console_handler = RichHandler(
    # rich_tracebacks=True, # does not work with custom formatters
    markup=True,
    show_level=False,
    show_time=False,
    show_path=False,
)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)
console_handler.formatter = console_formatter

logger = logging.getLogger(APP_LOGGER_NAME)
logging.getLoggerClass().trace = trace  # type: ignore[attr-defined]
logger.addHandler(console_handler)
