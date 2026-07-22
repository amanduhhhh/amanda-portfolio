#!/bin/bash

# cd into the project folder
cd ~/amanda-portfolio

# make sure the VPS repo matches the latest main from GitHub
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build
