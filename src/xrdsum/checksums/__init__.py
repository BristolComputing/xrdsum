"""xrdsum.checksums package"""

from __future__ import annotations

from ._base import Checksum
from ._crc32c import CRC32C
from .adler32 import Adler32

AVAILABLE_CHECKSUM_TYPES = {
    "adler32": Adler32,
    "crc32c": CRC32C,
}
__all__ = ["AVAILABLE_CHECKSUM_TYPES", "CRC32C", "Adler32", "Checksum"]
