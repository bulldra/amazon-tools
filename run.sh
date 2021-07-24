#!/bin/bash

if [ $# != 1 ]; then
	exit
fi

mkdir -p work 2>/dev/null
cp ${HOME}/Library/Containers/com.amazon.Kindle/Data/Library/Application\ Support/Kindle/Cache/KindleSyncMetadataCache.xml work/
docker-compose run --entrypoint 'python /data/src/kindle_lib.py' amazon-tools ./work/KindleSyncMetadataCache.xml --out ./work/kindle_lib.tsv
docker-compose down

docker-compose run --entrypoint "python /data/src/main.py" amazon-tools $1
docker-compose down
