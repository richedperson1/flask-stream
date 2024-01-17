import json
from flask import Flask, stream_with_context, Response
import time

app = Flask(__name__)


@app.route('/stream',methods = ["GET","POST"])
def stream_data():
    url = ""
    def generate_data():
        for i in range(100):
            if i==0:
                url = "random_data_url"
                continue
            data = {"chunk_id": i, "data": f"Data chunk {i}"}  # Construct JSON object
            yield f": hellow-{i}\n\n"
            # yield f"data: {json.dumps(data)}\n\n"  # Yield as JSON with newlines
        data = {"data_url":url,"page_num":1} 
        yield f"data: {json.dumps(data)}\n\n"
    return app.response_class(stream_with_context(generate_data()), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
