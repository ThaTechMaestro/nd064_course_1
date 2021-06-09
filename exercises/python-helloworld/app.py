from flask import Flask, json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def health_check():
    response = app.response_class(
        response=json.dumps({"result":"Ok - healthy"}),
        status = 200,
        mimetype='application/json'
    )

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success", "code":0, "data":{"UserCount":140,"UserCountActive":23}}),
        status = 200,
        mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
