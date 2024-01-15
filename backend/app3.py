from flask import Flask, stream_with_context, Response
import time

app = Flask(__name__)

@app.route('/stream-data')
def stream_data():
    def generate_data():
        for i in range(10):
            print(f"Data chunk {i}\n")
            yield f"Data chunk {i}\n"  # Yield the data chunk first
            # flush = True  # Then set flush to True (corrected order)
            time.sleep(1)

    response = Response(stream_with_context(generate_data()), mimetype='text/event-stream')
    response.headers['Content-Type'] = 'text-/event-stream'
    return response

if __name__ == '__main__':
    app.run(debug=True)
