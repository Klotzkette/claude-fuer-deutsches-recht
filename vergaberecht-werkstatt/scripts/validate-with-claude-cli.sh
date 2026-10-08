#!/usr/bin/env bash
# Schaerfere Validierung mit der offiziellen Claude Code CLI.
# Faengt genau das ab, was der User-Client beim "Install from .zip" prueft.
#
# Voraussetzung:
#   npm install -g @anthropic-ai/claude-code
#
# Aufruf:
#   ./scripts/validate-with-claude-cli.sh           # alle Plugins + marketplace
#   ./scripts/validate-with-claude-cli.sh <slug>    # nur eines

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v claude >/dev/null 2>&1; then
  echo "FEHLER: claude CLI fehlt. Installation:" >&2
  echo "  npm install -g @anthropic-ai/claude-code" >&2
  exit 2
fi

VERSION="$(claude --version 2>&1 | head -1)"
echo "Claude CLI: $VERSION"
echo ""

FAILED=0

validate_one() {
  local target="$1"
  local label="$2"
  if ! claude plugin validate --strict "$target" 2>&1 | tail -10; then
    echo "FEHLER bei $label" >&2
    FAILED=$((FAILED + 1))
  fi
  echo ""
}

if [ $# -gt 0 ]; then
  for slug in "$@"; do
    if [ ! -d "$slug" ]; then
      echo "FEHLER: $slug nicht gefunden" >&2
      exit 2
    fi
    echo "=== Plugin: $slug ==="
    validate_one "$slug" "$slug"
  done
else
  echo "=== Marketplace ==="
  validate_one ".claude-plugin/marketplace.json" "marketplace.json"

  echo "=== Alle Plugins (strict) ==="
  python3 -c "
import json
m = json.load(open('.claude-plugin/marketplace.json'))
for p in m['plugins']:
    print(p['name'])
" | while read -r slug; do
    if [ -d "$slug" ]; then
      echo "--- $slug ---"
      if ! claude plugin validate --strict "$slug" 2>&1 | grep -E '(passed|FAIL|error|warn)' | tail -3; then
        FAILED=$((FAILED + 1))
      fi
    else
      echo "WARN: $slug nicht im Repo-Root gefunden" >&2
    fi
  done
fi

if [ "$FAILED" -gt 0 ]; then
  echo ""
  echo "FEHLER: $FAILED Plugin(s) sind nicht strict-konform." >&2
  exit 1
fi

echo ""
echo "OK: Alle Plugins haben 'claude plugin validate --strict' bestanden."
