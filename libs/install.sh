#!/bin/sh

# Update Raspian
sudo apt update
sudo apt -y full-upgrade

# Install omxplayer
sudo apt install -y omxplayer

# Install gpiozero
sudo apt install -y python-gpiozero

# Install SPI-Py
cd ./SPI-Py
sudo python setup.py install
cd ..