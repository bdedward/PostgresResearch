FROM chrisioa/dsamdb:latest

COPY postgresql.conf /tmp/
COPY server.crt /tmp/
COPY server.key /tmp/
COPY root.crt /tmp/

#RUN chmod 0640 /tmp/*

COPY mutate.sh /docker-entrypoint-initdb.d/


