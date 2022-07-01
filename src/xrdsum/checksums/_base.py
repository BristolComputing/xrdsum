from __future__ import annotations

from typing import Any, Iterable, Protocol


class Checksum(Protocol):

    name: str = "Unknown"
    value: str = "N/A"
    bytes_read: int = 0
    number_of_buffers_read: int = 0

    def int_to_hex(self, value: int) -> str:
        pass

    def hex_to_int(self, value: str) -> int:
        pass

    def calculate(self, file_buffer: Iterable[Any]) -> str:
        pass
