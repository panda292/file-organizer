#!/usr/bin/env bash
# demo.sh — reproduce demo files and run file_organizer
BASE="$(pwd)"
SRC="$BASE/demo_src"
DEST="$BASE/demo_out"

# prepare demo folders
rm -rf "$SRC" "$DEST"
mkdir -p "$SRC" "$DEST"

# create sample files
cd "$SRC" || exit 1
touch photo1.jpg doc1.pdf song1.mp3 video1.mp4 script1.py archive1.zip report.docx note.txt

# run dry-run
echo "=== Dry run ==="
python3 ../file_organizer.py --source "$SRC" --dest "$DEST" --dry-run

# run copy
echo "=== Copy run ==="
python3 ../file_organizer.py --source "$SRC" --dest "$DEST"

# reset files and run move (clean)
rm -rf "$SRC" "$DEST"
mkdir -p "$SRC" "$DEST"
cd "$SRC" || exit 1
touch photo1.jpg doc1.pdf song1.mp3 video1.mp4 script1.py archive1.zip report.docx note.txt

echo "=== Move run ==="
python3 ../file_organizer.py --source "$SRC" --dest "$DEST" --move

echo "Demo finished. Destination contents:"
ls -R "$DEST"
