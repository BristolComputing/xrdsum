from __future__ import annotations

import logging
from typing import Any

import typer

from .backends import FILE_SYSTEMS
from .checksums import AVAILABLE_CHECKSUM_TYPES, Checksum
from .logger import console_handler, logger

app = typer.Typer()


@app.callback()
def logging_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
) -> Any:
    # verbose is debug
    trace = verbose and debug
    verbose = debug or verbose
    debug = verbose
    log_level = logging.INFO

    if debug:
        log_level = logging.DEBUG
    if trace:
        log_level = logging.TRACE  # type: ignore[attr-defined]
    logger.setLevel(log_level)
    console_handler.setLevel(log_level)


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
    file_system: str = typer.Option(
        default="HDFS",
        help="File system to use for reading the file",
    ),
) -> None:
    """
    Get the checksum of a file.
    """
    # convert from MB to bytes
    read_size *= 1024 * 1024
    try:
        hdfs = FILE_SYSTEMS[file_system](file_path, read_size)
    except KeyError:
        raise typer.Exit(
            f"Unknown file system: {file_system}",
            errno=1,
        )
    try:
        checksum: Checksum = AVAILABLE_CHECKSUM_TYPES[checksum_type]()
    except KeyError:
        raise typer.Exit(
            f"Unknown checksum type: {checksum_type}",
            errno=1,
        )
    checksum = hdfs.get_checksum(checksum)
    typer.echo(checksum.value)


@app.command()
def verify(
    file_path: str,
    checksum_value: str,
    checksum_type: str = "adler32",
) -> None:
    """
    Check if a file has the correct checksum.
    """
    raise NotImplementedError()


def main() -> Any:
    return app()
