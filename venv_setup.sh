#!/bin/bash

if [[ ! -d venv ]]
then
    python3.12 -m venv venv
fi

source venv/bin/activate

python3.12 -m pip install -U pip
python3.12 -m pip install -U -r requirements.txt
