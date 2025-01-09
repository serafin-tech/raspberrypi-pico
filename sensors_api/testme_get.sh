#!/bin/bash

source .env

curl -s -X GET http://127.0.0.1:8000/sensors \
    -H 'accept: application/json' \
    -H "X-API-Key: ${X_API_KEY}" | jq

