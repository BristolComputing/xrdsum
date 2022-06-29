from __future__ import annotations

from typing import Any

import typer

app = typer.Typer()


@app.command()
def get(
    file_path: str,
    store_result: bool = False,
    checksum_type: str = "adler32",
    read_size: int = typer.Option(
        default=64,
        help="""
Size [in MB] of the chunks to read from the file.
Should be a power of 2, and near (but not larger than) the stripe size.
Smaller values will use less memory, larger sizes may have benefits in IO performance.
""",
    ),
    storage_catalog: str = typer.Option(
        default="/etc/xrootd/storage.xml",
        help="Path to the CMS storage catalog",
    ),
    verbose: bool = False,
    debug: bool = False,
) -> None:
    """
    Get the checksum of a file.
    """
    raise NotImplementedError()


@app.command()
def verify(
    file_path: str,
    checksum_value: str,
    checksum_type: str = "adler32",
    verbose: bool = False,
    debug: bool = False,
) -> None:
    """
    Check if a file has the correct checksum.
    """
    raise NotImplementedError()


def main() -> Any:
    return app()
