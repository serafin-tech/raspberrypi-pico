#!/bin/bash

mpremote fs cp sensors_device/*.py :
mpremote soft-reset
minicom --device=/dev/ttyACM0

