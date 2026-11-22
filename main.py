#!/usr/bin/env python3
"""Publish the 22 November 2026 world-news poster (news-image-20261122).

The poster itself is a fixed file, entry.png: a 1024x1024 newspaper front
page drawn by build_image.py from reporting published on 22 November 2026
(COP31 collapsing in Antalya, Iran striking Bahrain, the S&P 500 falling
3.7%, and 22 further stories). This script does not draw anything. It
loads the bundled PNG, confirms it is really a PNG of the size the
competition allows, and writes that exact byte stream to the output
directory as entry.png. It touches no network and holds no state, so a
second run produces a byte-identical file.
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"
LIMIT = 1_048_576  # 1 MiB, the competition maximum
SIGNATURE = b"\x89PNG\r\n\x1a\n"
TRAILER = b"\x00\x00\x00\x00IEND\xaeB`\x82"  # the 12-byte IEND chunk
EXPECTED = (1024, 1024)


def load_bundled_poster():
    """Read entry.png and fail loudly unless it meets every limit."""
    try:
        blob = BUNDLED.read_bytes()
    except OSError as err:
        raise SystemExit(f"cannot read bundled poster: {err}")
    if blob[:8] != SIGNATURE:
        raise SystemExit("bundled poster is not a PNG file")
    if not blob.endswith(TRAILER):
        raise SystemExit("bundled poster is truncated: no IEND chunk")
    if len(blob) > LIMIT:
        raise SystemExit(
            f"bundled poster is {len(blob)} bytes, over the {LIMIT} limit")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if (width, height) != EXPECTED:
        raise SystemExit(
            f"bundled poster is {width}x{height}, expected 1024x1024")
    return blob


def publish(blob):
    """Write the poster to MAKEFUN_OUTPUT_DIR/entry.png and re-check it."""
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(blob)
    if target.read_bytes() != blob:
        raise SystemExit("written poster differs from the bundled poster")


def main():
    publish(load_bundled_poster())


if __name__ == "__main__":
    main()
