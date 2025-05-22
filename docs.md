docker run --name mongodb -d \
-p 27017:27017 \
-e MONGODB_INITDB_ROOT_USERNAME=user \
-e MONGODB_INITDB_ROOT_PASSWORD=password \
-v mongodb-data:/data/db \
--network metabase_app \
mongodb/mongodb-community-server

docker run -d -p 3000:3000 --name metabase \
--network metabase_app \
metabase/metabase

docker run --name mongosh --network \
 mongosh mongodb://mongodb --eval "show dbs"

### Comandos

docker network create metabase_app

docker stop mongodb && docker rm mongodb

docker logs container_name

docker network inspect metabase_app
