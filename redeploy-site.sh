#!/bin/bash


tmux kill-server 2>/dev/null || true
cd ~/amanda-portfolio
git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt

# start a new detached tmux session that runs the Flask server
tmux new-session -d -s flask-server -c ~/amanda-portfolio \; \
  send-keys "source python3-virtualenv/bin/activate && flask run --host=0.0.0.0" Enter
