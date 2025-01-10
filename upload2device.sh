#!/bin/bash

mpremote fs cp sensors_device/*.py :
sleep 2
mpremote reset
sleep 2
mpremote connect port:/dev/ttyACM0
#minicom --device=/dev/ttyACM0

