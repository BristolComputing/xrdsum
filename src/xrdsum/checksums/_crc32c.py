from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import crc32c

from ..logger import APP_LOGGER_NAME, get_logger
from ._base import Checksum

log = get_logger(APP_LOGGER_NAME)


class CRC32C(Checksum):
    name: str = "crc32c"

    def calculate(self, file_buffer: Iterable[Any]) -> str:
        value = crc32c.CRC32CHash()
        bytes_read = 0
        number_of_buffers_read = 0
        for buffer in file_buffer:
            value.update(buffer)
            bytes_read += len(buffer)
            number_of_buffers_read += 1
            log.trace(
                "%s: %s %s %s",
                self.name,
                value.hexdigest(),
                len(buffer),
                bytes_read,
            )

        self.value = value.hexdigest()
        self.bytes_read = bytes_read
        self.number_of_buffers_read = number_of_buffers_read

        return self.value
