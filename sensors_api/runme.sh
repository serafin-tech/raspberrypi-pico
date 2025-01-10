#!/bin/bash

source ../venv/bin/activate

uvicorn api:app --reload --host=0.0.0.0 --port=8000 --timeout-keep-alive 1 --http httptools
