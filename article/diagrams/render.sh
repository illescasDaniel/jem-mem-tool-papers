#!/usr/bin/env bash
# Re-render the article images from the PlantUML sources (needs plantuml + librsvg).
set -euo pipefail
cd "$(dirname "$0")"
for f in tiers lifecycle write-h recall-h architecture consolidation session-flow scopes; do
  plantuml -tsvg -o ../images "$f.puml"
  rsvg-convert -z 2 -o "../images/$f.png" "../images/$f.svg"
done
python3 make_growth.py && rsvg-convert -z 2 -o ../images/memory-growth.png ../images/memory-growth.svg
python3 -c "import re,sys" 
