from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import eventlet
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Start a background task to emit random data every 2 seconds
    eventlet.spawn(generate_random_data)

def generate_random_data():
    ind = 0
    while ind<100:
        random_value = random.randint(1, 100)
        emit('random_data', {'value': random_value})
        eventlet.sleep(1)
        ind+=1

if __name__ == '__main__':
    socketio.run(app, debug=True)
