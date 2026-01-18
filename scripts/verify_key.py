#!/usr/bin/env python3
"""
Verify GPG key files have course signature.

Usage:
    python verify_key.py <keyfile.asc> [keyfile2.asc ...]
"""

import sys
import os

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gpg_utils import verify_key_file, Colors


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <keyfile.asc> [keyfile2.asc ...]")
        print("\nVerifies if GPG public key files are signed by the CPSC4130 course key.")
        sys.exit(1)
    
    # Disable colors if not a TTY
    if not sys.stdout.isatty():
        Colors.disable()
    
    all_valid = True
    
    for keyfile in sys.argv[1:]:
        is_valid, message, key_info = verify_key_file(keyfile)
        
        if is_valid:
            status = f"{Colors.GREEN}✓{Colors.NC}"
            validity = f"{Colors.GREEN}VALID{Colors.NC}"
        else:
            status = f"{Colors.RED}✗{Colors.NC}"
            validity = f"{Colors.RED}INVALID{Colors.NC}"
            all_valid = False
        
        uid_str = f" ({key_info.uid})" if key_info and key_info.uid else ""
        print(f"{status} {keyfile}{uid_str}")
        print(f"  ({validity}) {message}")
        print()
    
    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()