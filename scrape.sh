#!/bin/bash

LAUNCH_CMD="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222"
SCRAPE_URL="https://www.jointaro.com/course/crash-course-data-structures-and-algorithms-concepts/course-welcome/"

export SCRAPE_URL

eval $LAUNCH_CMD

sleep 10

source /venv/bin/activate

python dl.py

deactivate

