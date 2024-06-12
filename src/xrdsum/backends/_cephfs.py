"""Implementation of the CephFS backend."""
# we want non-top-level imports to avoid pulling CephFS/cephsum dependencies early
# pylint: disable=import-outside-toplevel
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..checksums import Checksum
from ._base import XrdsumBackend

CONF = "/etc/ceph/ceph.conf"
KEYRING = "/etc/ceph/ceph.client.xrootd.keyring"
USER = "client.xrootd"
XATTR_TEMPLATE = "user.xrdsum.{}"


@dataclass
class CephSettings:
    """Settings for the CephFS backend."""

    config_file: str = CONF
    keyring: str = KEYRING
    user: str = USER
    read_size: int = 64 * 1024 * 1024


def get_ceph_client(settings: CephSettings) -> Any:
    """Retrieving the CephFS client to execute operations on CephFS."""
    import rados  # pylint: disable=import-error # type: ignore[import-not-found]

    try:
        client = rados.Rados(
            conffile=settings.config_file,
            conf={"keyring": settings.keyring},
            name=settings.user,
        )
        client.connect()
    except rados.Error as exc:
        msg = "Failed to connect to Ceph cluster"
        raise RuntimeError(msg) from exc
    return client


def path_to_oid(path: str) -> str:
    """Convert a path to an object ID."""
    # 1. get the inode from the path
    # 2. Convert the inode to hex and add the chunk0
    # 3. return the oid
    inode = Path(path).stat().st_ino
    return f"{inode:x}.{0:08x}"


class CephFSBackend(XrdsumBackend):
    """Implementation of the CephFS backend."""

    client: Any
    settings: CephSettings

    def __init__(
        self, file_path: str, read_size: int, **kwargs: dict[str, Any]
    ) -> None:
        """CephFS backend requires at least the file_path and read_size"""
        self.file_path = file_path
        self.settings = CephSettings(
            read_size=read_size,
            **kwargs,  # type: ignore[arg-type]
        )
        self.client = get_ceph_client(self.settings)

    def get_checksum(self, checksum: Checksum) -> Checksum:
        raise NotImplementedError()

    def store_checksum(self, checksum: Checksum, force: bool = False) -> None:
        raise NotImplementedError()
