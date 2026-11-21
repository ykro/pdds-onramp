#!/usr/bin/env bash
set -euo pipefail

# BUG 1 (CA-1.1): falta validar que el archivo exista y salir con código 1 si no existe.
LOG_FILE="${1:-}"

TOTAL_REQUESTS=$(wc -l < "$LOG_FILE" | tr -d ' ')
# BUG 2 (CA-1.2): este patrón cuenta códigos 4xx en lugar de 5xx.
ERRORS_5XX=$(awk '$4 ~ /^4[0-9][0-9]$/ { count++ } END { print count + 0 }' "$LOG_FILE")
TOP_ENDPOINTS=$(awk '{ print $3 }' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 3 | awk '{ printf "%s:%s ", $2, $1 }' | sed 's/ $//')

echo "total_requests=${TOTAL_REQUESTS}"
echo "errors_5xx=${ERRORS_5XX}"
echo "top_endpoints=${TOP_ENDPOINTS}"
