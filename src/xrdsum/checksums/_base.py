"""Definition of the Checksum protocol."""
from __future__ import annotations

import struct
from typing import Any, Iterable, Protocol


def int_to_hex(value: int) -> str:
    # return hex(value)[2:]
    return "".join([f"{x:02x}" for x in struct.pack(">I", value)]).lower()


def hex_to_int(value: str) -> int:
    return int(value, 16)


class Checksum(Protocol):
    """Base protocol for checksum implementations."""

    name: str = "Unknown"
    value: str = "N/A"
    bytes_read: int = 0
    number_of_buffers_read: int = 0

    def calculate(self, file_buffer: Iterable[Any]) -> str:
        """Calculates the checksum"""
        raise NotImplementedError()
