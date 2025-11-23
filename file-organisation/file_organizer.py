#!/usr/bin/env python3
"""
file_organizer.py

Organizes files in a source directory into categorized folders inside a destination directory.
Supports dry-run, recursive scan, move/copy option, logging, and custom categories.
"""

import argparse
import logging
import os
import shutil
import sys
from pathlib import Path
from datetime import datetime

# Default mapping of extensions to folder names
DEFAULT_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".odt"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Code": {".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".json", ".sql"},
    "Executables": {".exe", ".msi", ".sh", ".bat"},
    "Ebooks": {".epub", ".mobi", ".azw3"},
}

IGNORED_DIRS = {".git", "__pycache__"}


def setup_logger(logfile: Path = None, level=logging.INFO):
    logger = logging.getLogger("file_organizer")
    logger.setLevel(level)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.handlers = []
    logger.addHandler(sh)
    if logfile:
        fh = logging.FileHandler(logfile, encoding="utf-8")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger


def extension_to_category(ext: str, categories: dict):
    ext = ext.lower()
    for cat, exts in categories.items():
        if ext in exts:
            return cat
    return "Others"


def ensure_dir(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def resolve_duplicate(dest_path: Path) -> Path:
    if not dest_path.exists():
        return dest_path
    stem = dest_path.stem
    suffix = dest_path.suffix
    parent = dest_path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_once(source: Path, dest: Path, categories: dict, move: bool, dry_run: bool,
                  recursive: bool, logger=None):
    logger = logger or logging.getLogger("file_organizer")
    logger.info(f"Scanning: {source} (recursive={recursive})")

    if recursive:
        files = [p for p in source.rglob("*") if p.is_file()]
    else:
        files = [p for p in source.iterdir() if p.is_file()]

    logger.info(f"Found {len(files)} file(s)")

    for f in files:
        if any(part in IGNORED_DIRS for part in f.parts):
            continue

        ext = f.suffix.lower()
        category = extension_to_category(ext, categories)
        category_dir = dest / category
        ensure_dir(category_dir)

        target = category_dir / f.name
        target = resolve_duplicate(target)

        action = "move" if move else "copy"

        if dry_run:
            logger.info(f"[DRY RUN] Would {action} '{f}' -> '{target}'")
            continue

        try:
            if move:
                shutil.move(str(f), str(target))
                logger.info(f"Moved '{f}' -> '{target}'")
            else:
                shutil.copy2(str(f), str(target))
                logger.info(f"Copied '{f}' -> '{target}'")
        except Exception as e:
            logger.error(f"Failed to {action} '{f}' -> '{target}': {e}")


def parse_args():
    parser = argparse.ArgumentParser(description="Organize files in a folder by extension.")
    parser.add_argument("--source", "-s", type=Path, required=True, help="Source directory")
    parser.add_argument("--dest", "-d", type=Path, required=True, help="Destination directory")
    parser.add_argument("--move", action="store_true", help="Move files instead of copying")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without doing them")
    parser.add_argument("--recursive", action="store_true", help="Scan directories recursively")
    parser.add_argument("--log", type=Path, default=None, help="Optional log file path")
    return parser.parse_args()


def main():
    args = parse_args()
    source = args.source.expanduser().resolve()
    dest = args.dest.expanduser().resolve()

    if not source.exists() or not source.is_dir():
        print(f"Source directory does not exist: {source}")
        sys.exit(1)

    ensure_dir(dest)

    logger = setup_logger(args.log)
    start_time = datetime.now()
    logger.info(f"Starting file organizer at {start_time.isoformat()}")

    try:
        organize_once(
            source, dest, DEFAULT_CATEGORIES,
            args.move, args.dry_run, args.recursive, logger=logger
        )
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")

    end_time = datetime.now()
    logger.info(f"Finished at {end_time.isoformat()} (Duration: {end_time - start_time})")


if __name__ == "__main__":
    main()
