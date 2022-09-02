from __future__ import annotations

from typing import Protocol


class StorageCatalog(Protocol):
    def __init__(self, config: str | None = None, protocol: str | None = None) -> None:
        raise NotImplementedError()

    def lfn2pfn(self, lfn: str) -> str:
        """Converts logical filename to physical filename"""
        raise NotImplementedError()
