#!/bin/bash

source .env

TIMESTAMP=$(date --iso-8601=seconds)

curl -X POST http://127.0.0.1:8000/sensors \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: ${X_API_KEY}" \
  -d "{
    \"regname\": \"param\",
    \"value\": \"string_val\",
    \"dt\": \"${TIMESTAMP}\"
  }"
