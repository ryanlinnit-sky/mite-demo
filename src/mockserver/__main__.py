"""mockserver

Usage:
    mockserver [-d | --daemon] [-s | --stop] [options]

Options:
    -d --daemon             Run the mockserver as a daemon
    -s --stop               Stop a running mockserver daemon
    --log-level=LEVEL       Set logger level: DEBUG, INFO, WARNING, ERROR, CRITICAL [default: INFO]

"""  # noqa: E501


import contextlib
import logging
import os
import subprocess
import sys

import psutil
from docopt import docopt

from mockserver import MockServer
from mockserver.endpoints import ENDPOINTS

_PID_FILE = "/tmp/mockserver.pid"
logger = logging.getLogger(__name__)


def run_daemon():
    def spawn_mockserver():
        cmd = ["mockserver"]

        _env = os.environ
        _env["MOCKSERVER_DAEMON"] = "true"

        proc = subprocess.Popen(cmd, stdin=None, stdout=None, stderr=None, env=_env)
        logger.info(f"Spawned mockserver with {proc.pid=}")
        with open(_PID_FILE, "w+") as fd:
            fd.write(f"{proc.pid}")

    if os.path.exists(_PID_FILE):
        with open(_PID_FILE) as fd:
            pid = int(fd.readline().strip())

        try:
            psutil.Process(pid)
            logger.info(f"Mockserver already running under {pid=}")
        except psutil.NoSuchProcess:
            os.unlink(_PID_FILE)
            spawn_mockserver()
    else:
        spawn_mockserver()


def stop_daemon():
    if not os.path.exists(_PID_FILE):
        return

    with open(_PID_FILE) as fd:
        pid = int(fd.readline().strip())

    with contextlib.suppress(psutil.NoSuchProcess):
        proc = psutil.Process(pid)
        proc.terminate()
        logger.info(f"Terminated {pid=}")

    os.unlink(_PID_FILE)


def setup_logging(opts):
    if os.environ.get("MOCKSERVER_DAEMON"):
        logging.getLogger("werkzeug").disabled = True
        cli = sys.modules["flask.cli"]
        cli.show_server_banner = lambda *x: None
    else:
        logging.basicConfig(
            level=opts["--log-level"], format="<%(levelname)s> %(message)s", force=True,
        )


def main():
    opts = docopt(__doc__)

    setup_logging(opts)

    if opts["--daemon"]:
        run_daemon()
    elif opts["--stop"]:
        stop_daemon()
    else:
        app = MockServer()

        for endpoint in ENDPOINTS:
            app.add_endpoint(*endpoint)

        app.run()


if __name__ == "__main__":
    main()
