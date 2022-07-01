from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..checksums import Checksum
from ._base import XrdsumBackend

CONF = "/etc/ceph/ceph.conf"
KEYRING = "/etc/ceph/ceph.client.xrootd.keyring"
USER = "client.xrootd"


@dataclass
class CephSettings:
    config_file: str = CONF
    keyring: str = KEYRING
    user: str = USER
    read_size: int = 64 * 1024 * 1024


def get_ceph_client(settings: CephSettings) -> Any:
    import cephsum

    client = cephsum.cephtools.cluster_connect(
        conffile=settings.config_file,
        keyring=settings.keyring,
        name=settings.user,
    )
    return client


class CephFSBackend(XrdsumBackend):
    client: Any
    settings: CephSettings

    def __init__(
        self, file_path: str, read_size: int, **kwargs: dict[str, Any]
    ) -> None:
        self.file_path = file_path
        self.settings = CephSettings(
            read_size=read_size,
            **kwargs,  # type: ignore[arg-type]
        )

    def get_checksum(self, checksum: Checksum) -> Checksum:
        raise NotImplementedError()

    def store_checksum(self, checksum: Checksum, force: bool = False) -> None:
        raise NotImplementedError()
