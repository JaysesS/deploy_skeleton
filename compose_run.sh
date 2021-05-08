#!/bin/sh

# docker volume create --name=database_data

mode=$1

if [ "$mode" = "" ] && ( [ ! "$mode" = "prod" ] | [ ! "$mode" = "test" ] );
then
    echo "SET \"test\" OR \"prod\" in args!"
    exit 1
fi

echo "Mode: $mode"

if [ "$mode" = "prod" ];
then
    cat $(pwd)/project.env > .env
elif [ "$mode" = "test" ];
then
    cat $(pwd)/project.test.env > .env
fi

docker-compose up -d --build