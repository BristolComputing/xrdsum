"""Module for calculating crc32c checksums."""
from __future__ import annotations

import logging
from typing import Any, Iterable

import crc32c

from ..logger import APP_LOGGER_NAME
from ._base import Checksum, int_to_hex

log = logging.getLogger(APP_LOGGER_NAME)


class Crc32c(Checksum):
    """crc32c checksum"""

    name: str = "crc32c"

    def calculate(self, file_buffer: Iterable[Any]) -> str:
        value = 1
        bytes_read = 0
        number_of_buffers_read = 0
        for buffer in file_buffer:
            value = crc32c.crc32c(buffer, value)
            bytes_read += len(buffer)
            number_of_buffers_read += 1
            log.trace(  # type: ignore[attr-defined]
                "%s: %s %s %s",
                self.name,
                int_to_hex(value),
                len(buffer),
                bytes_read,
            )

        self.value = int_to_hex(value)
        self.bytes_read = bytes_read
        self.number_of_buffers_read = number_of_buffers_read

        return self.value
