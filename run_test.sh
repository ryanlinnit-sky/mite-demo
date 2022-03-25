#!/bin/bash

# Start grafana and prometheus docker containers
docker-compose -f provisioning/docker_compose.yml up -d

# Start the mockserver
mockserver -d

# Start the mite components
mite runner --controller-socket=tcp://127.0.0.1:14301 --message-socket=tcp://127.0.0.1:14302 &
mite duplicator --message-socket=tcp://0.0.0.0:14302 tcp://0.0.0.0:14303 &
mite stats --stats-in-socket=tcp://127.0.0.1:14303 --stats-out-socket=tcp://0.0.0.0:14305 --stats-include-processors=mite,mite_http &
mite prometheus_exporter --stats-out-socket=tcp://127.0.0.1:14305 --web-address=0.0.0.0:9301 &

mite controller --controller-socket=tcp://0.0.0.0:14301 --message-socket=tcp://127.0.0.1:14302 application.scenarios:quick_scenario --config application.config:config &

echo "Open grafana in your browser http://localhost:3000/d/2_KG1Va7z/mite-docker?orgId=1&refresh=10s"