# CPSC4130 GPG Key Exchange

A repository for exchanging GPG public keys for the key signing assignment.

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd gpg-keyring

# Import the course key
gpg --import course_key.asc
```

## Repository Structure

```
gpg-keyring/
├── course_key.asc              # Course public key
├── keys/                       # Everyone's public keys (course-signed)
│   ├── ab123.asc
│   └── ...
├── signed/                     # Signatures made by each person
│   ├── ab123/                  # Signatures made BY ab123
│   │   ├── cd456.asc
│   │   └── ...
│   └── ...
├── scripts/
│   └── verify_pr_keys.sh       # CI verification script
├── sign_all.sh                 # Sign all verified keys
└── collect_signatures.sh       # Collect signatures on your key
```

## Workflow

### Step 1: Submit Your Key (One Time)

1. Fork this repository
2. Add your public key to `keys/<netid>.asc`
   - **Must be the course-signed version** (from Canvas after submission)
3. Create a Pull Request
   - CI will verify your key has the course signature
   - CI will reject files outside `keys/*.asc` or `signed/*/*.asc`
4. Wait for merge

### Step 2: Sign Everyone's Keys

```bash
# Pull latest keys
git pull

# Run the signing script
chmod +x sign_all.sh
./sign_all.sh

# Commit and push your signatures
git add signed/
git commit -m "Add signatures from <your-netid>"
git push  # or create PR
```

### Step 3: Collect Signatures on Your Key

```bash
# Pull latest (after others have signed)
git pull

# Run the collection script
chmod +x collect_signatures.sh
./collect_signatures.sh

# Export your key with all signatures
gpg --export --armor "your-email@yale.edu" > my_key_final.asc
```

## PR Rules

PRs may only add files matching:
- `keys/<netid>.asc` - Your course-signed public key
- `signed/<your-netid>/<other-netid>.asc` - Your signatures on others' keys

Any other files will be rejected by CI.

## Manual Verification

```bash
gpg --import keys/<netid>.asc
gpg --check-sigs <netid>@yale.edu
```

Look for:
```
sig!         A049C765A07C89D8 2026-01-17  CPSC4130
```

## Course Key Fingerprint

```
4DD5 B379 1798 E493 F649  9F8D A049 C765 A07C 89D8
```

## FAQ

**Q: CI failed on my key submission?**
A: You probably submitted your original key, not the course-signed version.

**Q: How do I check my progress?**
A: Run `./collect_signatures.sh`

**Q: Can adversarial keys sneak in?**
A: No (as long as you trust the manager of this repo) - CI verifies course signature on all keys in `keys/`. The `sign_all.sh` script also verifies before signing.