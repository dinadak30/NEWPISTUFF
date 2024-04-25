#!/bin/bash
python GPIO_Pin_power.py

rpicam-still -n --immediate -t 1 -o Background.jpg
echo 'Background Captured!'

echo 'Break beam sensor initialized. Waiting for objects...'

python Breakbeamtest.py

sleep 10

rpicam-still -n --immediate -t 1 -o Imagecapture.jpg
echo 'Image Captured! Beginning image analysis.'

python Subtraction_blue.py
echo 'Image Analyzed'

