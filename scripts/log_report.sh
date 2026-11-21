#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]] || [[ ! -f "$1" ]]; then
  echo "Error: log file not found: ${1:-<missing>}" >&2
  exit 1
fi

LOG_FILE="$1"

echo "TODO: implementa scripts/log_report.sh" >&2
exit 1
