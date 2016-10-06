#!/bin/bash
REPO=063507218586.dkr.ecr.eu-central-1.amazonaws.com

function upload() {
    echo "Building image $2 from directory $1"
    docker build -t $2 $1
    docker tag $2:latest $REPO/$2
    docker push $REPO/$2:latest
    echo "Done"
}

upload src/bot py-fb-bot/bot
upload src/backend py-fb-bot/backend
