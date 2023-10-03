# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


def set_default_cookies():
    response = make_response(jsonify(request.args))
    for k, v in request.args.items():
        response.set_cookie(k, v)
    return response


@app.get("/")
def index():
    return set_default_cookies()


@app.get("/path/to/page")
def path_to_page():
    return set_default_cookies()


if __name__ == "__main__":
    app.run()
