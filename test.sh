mkdir -p work 2>/dev/null
cp ${HOME}/Library/Containers/com.amazon.Kindle/Data/Library/Application\ Support/Kindle/Cache/KindleSyncMetadataCache.xml work/
docker-compose run -e "PYTHONPATH=./" --entrypoint "pytest /data/tests/" amazon-tools
