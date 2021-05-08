#!/usr/bin/fish

docker run --rm --name localpsql -d -p 5432:5432 --env-file=localpsql.env -v /var/lib/postgresql/data:/var/lib/postgresql/data postgres:12