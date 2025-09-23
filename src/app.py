# code from https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/

import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'hostname': socket.gethostname(),
    })


@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'status': 'up',
    }), 200


if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

