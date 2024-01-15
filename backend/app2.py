from flask import Flask, stream_with_context
import time

from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/stream-data')
@cross_origin(origin='*')
def stream_data():
    def generate_data():
        for i in range(100):  # Adjust the number of iterations as needed
            yield f"Data chunk {i}\n"
            time.sleep(0.2)  # Simulate a delay between chunks

    return app.response_class(stream_with_context(generate_data()), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
