#!/bin/bash

echo "\n\n\nMoving Posgres files to PGDATA directory...\n\n\n"

cp /tmp/postgresql.conf /var/lib/postgresql/data/
cp /tmp/server.key /var/lib/postgresql/data/
cp /tmp/server.crt /var/lib/postgresql/data/
cp /tmp/root.crt /var/lib/postgresql/data/

chown postgres /var/lib/postgresql/data/server.key
chown postgres /var/lib/postgresql/data/server.crt
chown postgres /var/lib/postgresql/data/root.crt
chmod 0600 /var/lib/postgresql/data/server.key
chmod 0600 /var/lib/postgresql/data/server.crt
chmod 0600 /var/lib/postgresql/data/root.crt
