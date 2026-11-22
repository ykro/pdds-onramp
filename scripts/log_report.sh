#!/usr/bin/env bash
set -euo pipefail

# Falla 1 (CA-1.1): sin argumento o con un archivo que no existe, el error que ve la persona es difícil de leer.
LOG_FILE="${1:-}"

TOTAL_REQUESTS=$(wc -l < "$LOG_FILE" | tr -d ' ')
# Falla 2 (CA-1.2): errors_5xx no coincide con lo que cuentas a mano en data/access.log.
ERRORS_5XX=$(awk '$4 ~ /^4[0-9][0-9]$/ { count++ } END { print count + 0 }' "$LOG_FILE")
TOP_ENDPOINTS=$(awk '{ print $3 }' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 3 | awk '{ printf "%s:%s ", $2, $1 }' | sed 's/ $//')

echo "total_requests=${TOTAL_REQUESTS}"
echo "errors_5xx=${ERRORS_5XX}"
echo "top_endpoints=${TOP_ENDPOINTS}"
