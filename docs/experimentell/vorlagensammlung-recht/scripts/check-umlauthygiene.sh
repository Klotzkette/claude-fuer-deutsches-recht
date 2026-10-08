#!/usr/bin/env bash
# Rückwärtskompatibler Aufruf; die plattformneutrale Implementierung ist Python.
set -euo pipefail

exec python3 "$(dirname "$0")/check-umlauthygiene.py"
