from __future__ import annotations

from ._hdfs import HDFSBackend

FILE_SYSTEMS = {
    "HDFS": HDFSBackend,
    "CephFS": None,
}

__all__ = ["FILE_SYSTEMS"]
