"""Definition of the Checksum protocol."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any


class Checksum(ABC):
    """Base protocol for checksum implementations."""

    name: str = "Unknown"
    value: str = "N/A"
    bytes_read: int = 0
    number_of_buffers_read: int = 0

    @abstractmethod
    def calculate(self, file_buffer: Iterable[Any]) -> str:
        """Calculates the checksum"""
        raise NotImplementedError()
