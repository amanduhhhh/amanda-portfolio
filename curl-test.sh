#!/bin/bash
# quick test for the timeline_post api

URL=http://localhost:5000/api/timeline_post

# random number so we can find our post later
NUM=$RANDOM
CONTENT="test post $NUM"

echo "POST a new post"
POST=$(curl -s -X POST "$URL" \
  -d "name=Test User" \
  -d "email=test@example.com" \
  -d "content=$CONTENT")
echo "$POST"

# grab the id from the response
ID=$(echo "$POST" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')
echo "created post with id $ID"

echo
echo "GET the timeline and check our post is there"
if curl -s "$URL" | grep -q "$CONTENT"; then
  echo "found it!"
else
  echo "not found :("
fi

echo
echo "DELETE the test post"
curl -s -X DELETE "$URL/$ID"
echo
