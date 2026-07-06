#!/usr/bin/env python3
"""Install Zone Memory Skill for Codex, Claude Code, or both."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

SKILL_NAME = "zone-memory"
REQUIRED_SKILL_FILES = (
    Path("SKILL.md"),
    Path("REFERENCE.md"),
    Path("references/agents_section.md"),
    Path("references/zone_operating_model_template.md"),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=("codex", "claude", "both"), required=True)
    parser.add_argument("--upgrade", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def install_targets(agent: str, home: Path) -> list[tuple[str, Path]]:
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex")).expanduser()
    available = {
        "codex": codex_home / "skills" / SKILL_NAME,
        "claude": home / ".claude" / "skills" / SKILL_NAME,
    }
    names = ("codex", "claude") if agent == "both" else (agent,)
    return [(name, available[name]) for name in names]


def validate_package(source: Path) -> str | None:
    for relative_path in REQUIRED_SKILL_FILES:
        if not (source / relative_path).is_file():
            return f"Invalid delivery package: missing {relative_path.as_posix()}"
    return None


def backup_path(destination: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = destination.with_name(f"{destination.name}.backup-{timestamp}")
    suffix = 1
    while candidate.exists():
        candidate = destination.with_name(
            f"{destination.name}.backup-{timestamp}-{suffix}"
        )
        suffix += 1
    return candidate


def staging_path(destination: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = destination.with_name(f".{destination.name}.installing-{timestamp}")
    suffix = 1
    while candidate.exists():
        candidate = destination.with_name(
            f".{destination.name}.installing-{timestamp}-{suffix}"
        )
        suffix += 1
    return candidate


def install_one(source: Path, destination: Path, upgrade: bool, dry_run: bool) -> str:
    backup = backup_path(destination) if destination.exists() else None
    if dry_run:
        if destination.exists() and not upgrade:
            return (
                f"would refuse to overwrite {destination}; "
                "rerun with --upgrade to back it up and replace it"
            )
        action = f"would install {source} -> {destination}"
        return f"{action}; would back up existing install to {backup}" if backup else action
    if destination.exists() and not upgrade:
        raise FileExistsError(
            f"{destination} already exists; rerun with --upgrade to back it up and replace it"
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = staging_path(destination)
    shutil.copytree(
        source,
        staging,
        ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"),
    )
    try:
        if backup:
            destination.rename(backup)
        staging.rename(destination)
    except Exception:
        if backup and backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    return f"installed {destination}" + (f"; previous version backed up to {backup}" if backup else "")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(__file__).resolve().parent
    source = root / "skills" / SKILL_NAME
    validation_error = validate_package(source)
    if validation_error:
        print(validation_error, file=sys.stderr)
        return 2
    home = Path.home()
    failures = 0
    for agent, destination in install_targets(args.agent, home):
        try:
            print(f"[{agent}] {install_one(source, destination, args.upgrade, args.dry_run)}")
        except (FileExistsError, OSError) as error:
            failures += 1
            print(f"[{agent}] ERROR: {error}", file=sys.stderr)
    if failures:
        return 1
    if not args.dry_run:
        print("Restart the Agent or open a new session to load Zone Memory Skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
