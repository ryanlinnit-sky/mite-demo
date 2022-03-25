from uuid import uuid4

from flask import Flask, jsonify


class MockServer:
    def __init__(self, host="0.0.0.0", port=5002, debug=False):
        super().__init__()
        self.host = host
        self.port = port
        self.debug = debug
        self.app = Flask(__name__)

    def add_endpoint(
        self,
        url,
        response="Hello World",
        status_code=200,
        methods=("GET",),
        headers=None,
    ):
        def callback(**kwargs):
            body = response if isinstance(response, str) else jsonify(response)
            return (body, status_code, headers)

        callback.__name__ = str(uuid4())

        self.app.add_url_rule(url, view_func=callback, methods=methods)

    def run(self):
        self.app.run(host=self.host, port=self.port, debug=self.debug)
