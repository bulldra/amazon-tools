mkdir -p work 2>/dev/null
cp ${HOME}/Library/Containers/com.amazon.Kindle/Data/Library/Application\ Support/Kindle/Cache/KindleSyncMetadataCache.xml work/
docker-compose run --entrypoint 'python /data/src/kindle_lib.py' amazon-tools
