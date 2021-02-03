import signal

from flask import Flask
from db_connector import *

app = Flask(__name__)


@app.route('/users/<id>')
def get_user(id):
    try:
        name = user_info(id)
        return "<H1 id='user'>" + name + "</H1>", 200
    except:
        return "<H1 id='error'>""no such user: " + id + "</H1>", 500


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)
