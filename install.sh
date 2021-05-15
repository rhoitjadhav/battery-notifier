#!/bin/bash

# Exit if any command fails
set -e

# Install Python3
sudo apt install python3

# dbus-python package dependencies
sudo apt install build-essential libpython3-dev libdbus-1-dev libdbus-glib-1-dev libgirepository1.0-dev

# Install pipenv
pip3 install pipenv

# Source .profile file
source ~/.profile

# Create virtual environment using pipenv and install dependencies
pipenv install