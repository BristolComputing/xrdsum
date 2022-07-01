from __future__ import annotations

from ..checksums import Checksum
from ._base import XrdsumBackend


class CephFSBackend(XrdsumBackend):
    def __init__(self, file_path: str, read_size: int):
        self.file_path = file_path
        self.read_size = read_size

    def get_checksum(self, checksum: Checksum) -> Checksum:
        raise NotImplementedError()

    def store_checksum(self, checksum: Checksum, force: bool = False) -> None:
        raise NotImplementedError()
