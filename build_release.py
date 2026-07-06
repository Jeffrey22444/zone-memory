#!/usr/bin/env python3
"""Build a ZIP release for Zone Memory Skill."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=Path("dist"))
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(__file__).resolve().parent
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    args.dist.mkdir(parents=True, exist_ok=True)
    archive_base = args.dist / f"zone-memory-skill-{version}"
    archive_path = archive_base.with_suffix(".zip")
    if archive_path.exists() and not args.overwrite:
        print(f"Refusing to overwrite existing archive: {archive_path}", file=sys.stderr)
        return 1
    if archive_path.exists():
        archive_path.unlink()
    built = shutil.make_archive(str(archive_base), "zip", root_dir=root)
    print(built)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
