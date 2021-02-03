import signal
from datetime import datetime

from flask import Flask, request, app
from db_connector import *

app = Flask(__name__)


@app.route('/users/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(id):
    if request.method == 'POST':
        try:
            name = request.json.get('user_name')
            add_user(id, name)
            return {'status': 'ok', 'user added': name}, 200
        except:
            return {'status': 'error', 'reason': "id already exists"}, 500

    elif request.method == 'GET':
        try:
            name = user_info(id)
            return {'status': 'ok', 'user name': name}, 200
        except:
            return {'status': 'error', 'reason': "no such id"}, 500

    elif request.method == 'DELETE':
        try:
            delete_user_id(id)
            return {'status': 'ok', 'user deleted': id}, 200
        except:
            return {'status': 'error', 'reason': "no such id"}, 500

    elif request.method == 'PUT':
        try:
            name = request.json.get('user_name')
            update_username(id, name)
            return {'status': 'ok', 'user updated': id}, 200
        except:
            return {'status': 'error', 'reason': "no such id"}, 500


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped', 200


app.run(host='127.0.0.1', debug=True, port=5000)
