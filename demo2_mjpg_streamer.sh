#!/bin/bash

MJPG_STREAMER_PATH="/home/pi/Downloads/sourcecode/mjpg-streamer/mjpg-streamer-experimental"

cd $MJPG_STREAMER_PATH
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
