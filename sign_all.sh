#!/bin/bash
# Sign all verified keys - wrapper script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/scripts/sign_all.py" "$@"