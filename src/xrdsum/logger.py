from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("xrdsum")

# add TRACE log level and function to logger
TRACE = 5
logging.addLevelName(TRACE, "TRACE")


def trace(
    self: logging.Logger, message: str, *args: list[Any], **kws: dict[str, Any]
) -> None:
    if self.isEnabledFor(TRACE):
        self._log(TRACE, message, args, **kws)  # type: ignore [arg-type]


logger.trace = trace  # type: ignore [attr-defined]
