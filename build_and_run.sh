#!/usr/bin/env bash

if [ "$WEBHOOK_URL" == "" ] ; then 
  echo "you should set WEBHOOK_URL in your environment or the service will not run"
  exit 1
fi

docker build -t addrum/synology-notifications:latest .
docker-compose up
