#!/bin/bash

mkdir -p ./work 2>/dev/null
mkdir -p ./log 2>/dev/null

docker-compose build
