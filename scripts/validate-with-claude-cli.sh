#!/usr/bin/env bash
# Schaerfere Validierung mit der offiziellen Plugin-CLI.
# Prüft Manifeste mit der installierten Plugin-CLI; kein interaktiver Importtest.
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
echo "Plugin-CLI: $VERSION"
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
  # Prozesssubstitution würde einen Fehler beim Einlesen nicht weitergeben.
  if ! PLUGIN_SOURCES="$(python3 - <<'PY'
import json
import sys

try:
    with open('.claude-plugin/marketplace.json', encoding='utf-8') as handle:
        marketplace = json.load(handle)
    if not isinstance(marketplace, dict) or not isinstance(marketplace.get('plugins'), list):
        raise ValueError('plugins muss eine Liste sein')
    rows = []
    for index, plugin in enumerate(marketplace['plugins'], start=1):
        if not isinstance(plugin, dict):
            raise ValueError(f'Plugin {index}: Objekt erwartet')
        for field in ('name', 'source'):
            value = plugin.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f'Plugin {index}: {field} muss eine nichtleere Zeichenfolge sein')
            if any(character in value for character in '\t\r\n\0'):
                raise ValueError(f'Plugin {index}: {field} enthält ungültige Steuerzeichen')
        rows.append(plugin['name'] + '\t' + plugin['source'])
    print('\n'.join(rows))
except (OSError, ValueError) as error:
    print(f'FEHLER: Marketplace-Quellen nicht lesbar: {error}', file=sys.stderr)
    sys.exit(1)
PY
)"; then
    exit 1
  fi

  if [ -n "$PLUGIN_SOURCES" ]; then
    while IFS=$'\t' read -r slug source; do
      if [ -d "$source" ]; then
        echo "--- $slug ---"
        validate_one "$source" "$slug"
      else
        echo "FEHLER: Quelle für $slug fehlt: $source" >&2
        FAILED=$((FAILED + 1))
      fi
    done <<< "$PLUGIN_SOURCES"
  fi
fi

if [ "$FAILED" -gt 0 ]; then
  echo ""
  echo "FEHLER: $FAILED Plugin(s) sind nicht strict-konform." >&2
  exit 1
fi

echo ""
echo "OK: Alle Plugins haben die strikte CLI-Validierung bestanden."
