#!/bin/bash
echo "RUN Bot"
python3 bot.py &
echo "RUN API"
python3 main.py
