"""xrdsum.checksums package"""
from __future__ import annotations

from ._base import Checksum
from .adler32 import Adler32
from .crc32c import Crc32c

AVAILABLE_CHECKSUM_TYPES = {
    "adler32": Adler32,
    "crc32c": Crc32c,
}
__all__ = ["Adler32", "Checksum", "Crc32c", "AVAILABLE_CHECKSUM_TYPES"]
