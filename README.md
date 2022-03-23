# Installation

If you have [mite-cli](https://pypi.org/project/mite-cli/) installed, you can run: 
```bash
mite-cli new my_project_dir -e
```

Activate your new virtual environment and off you go.

## Usage

The easiest way to run a full test is via the `run_test.sh` script:

```bash
./run_test.sh
```

And open [grafana](http://localhost:3000/d/2_KG1Va7z/mite-docker?orgId=1&refresh=10s) in your browser (Default username/password is `admin`/`admin`)

---
### Starting mock server

```bash
mockserver
```

### Journeys

```bash
mite journey test application.journeys:get_url1_journey --config application.config:config
```

### Scenarios

```bash
mite scenario test application.scenarios:quick_scenario --config application.config:config
```

### Start grafana/prometheus instances

```bash
docker-compose -f provisioning/docker_compose.yml up -d
```

### Start the mite components

```bash
mite runner --controller-socket=tcp://127.0.0.1:14301 --message-socket=tcp://127.0.0.1:14302 &
mite duplicator --message-socket=tcp://0.0.0.0:14302 tcp://0.0.0.0:14303 &
mite stats --stats-in-socket=tcp://127.0.0.1:14303 --stats-out-socket=tcp://0.0.0.0:14305 --stats-include-processors=mite,mite_http &
mite prometheus_exporter --stats-out-socket=tcp://127.0.0.1:14305 --web-address=0.0.0.0:9301 &

mite controller --controller-socket=tcp://0.0.0.0:14301 --message-socket=tcp://127.0.0.1:14302 application.scenarios:quick_scenario --config application.config:config &
```