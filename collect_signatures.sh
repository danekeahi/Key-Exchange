#!/bin/bash
# Collect signatures on your key - wrapper script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/scripts/collect_signatures.py" "$@"