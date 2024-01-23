# from flask import Flask, jsonify
# from threading import Timer

# app = Flask(__name__)

# def my_function():
#     # Your custom function logic goes here
#     # Example: print("Function called at", datetime.datetime.now())
#     print("Hello this is message")
#     return {"message": "Function called successfully!"}

# @app.route("/", methods=["GET"])
# def main():
#     # Return current time to demonstrate background job running
#     call_function_repeatedly()
#     return jsonify({"time": "datetime.datetime.now()"})

# def call_function_repeatedly():
#     # Call function and reschedule itself
#     my_function()
#     timer = Timer(20, call_function_repeatedly)
#     timer.daemon = True
#     timer.start()

# # Start the thread as soon as the application starts
# call_function_repeatedly()

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_apscheduler import APScheduler
import datetime
app = Flask(__name__)
scheduler = APScheduler()

def my_function():
    # Your custom function logic goes here
    # Example: print("Function called at", datetime.datetime.now())
    print("Hello this is message")
    return {"message": "Function called successfully!"}

@app.route("/", methods=["GET"])
def main():
    # Return current time to demonstrate background job running
    print("Hello this is message")
    return jsonify({"time": datetime.datetime.now()})

# Schedule the function to run every 20 seconds
scheduler.add_job(func=my_function, trigger="interval", seconds=2,id = "my_function")

if __name__ == "__main__":
    # scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)

