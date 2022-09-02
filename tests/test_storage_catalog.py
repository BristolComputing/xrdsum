from __future__ import annotations

import pytest

from xrdsum.storage_catalog import resolve_file_path


@pytest.fixture
def cli_param():
    return "cms|tests/storage.xml?direct"


@pytest.mark.parametrize(
    "lfn, pfn",
    [
        ("/store/user/johndoe/test.txt", "/xrootd/cms/store/user/johndoe/test.txt"),
        (
            "/xrootd/cms/store/user/johndoe/test.txt",
            "/xrootd/cms/store/user/johndoe/test.txt",
        ),
        ("/xrootd/othervo/test.txt", "/xrootd/othervo/test.txt"),
    ],
)
def test_resolve_file_path(cli_param, lfn, pfn):
    assert resolve_file_path(lfn, cli_param) == pfn
