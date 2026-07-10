#!/bin/bash

# cd into the project folder
cd ~/amanda-portfolio

# make sure the VPS repo matches the latest main from GitHub
git fetch && git reset origin/main --hard

# enter the virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# restart the service to pick up the changes
systemctl restart myportfolio.service
