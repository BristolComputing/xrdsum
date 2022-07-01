"""
Backends should implement how
1. to read a file (e.g. in chunks or not)
2. to calculate the checksum of a file
3. how to store the checksum of a file (e.g. in xattr)
"""
from __future__ import annotations

from typing import Protocol

from ..checksums import Checksum


class XrdsumBackend(Protocol):
    def __init__(
        self,
        file_path: str,
        read_size: int,
    ):
        pass

    def get_checksum(self, checksum: Checksum) -> Checksum:
        """Try to get checksum info from metadata, otherwise from file"""
        pass

    def store_checksum(self, checksum: Checksum, force: bool = False) -> None:
        """Store the checksum in the metadata of the file"""
        pass
