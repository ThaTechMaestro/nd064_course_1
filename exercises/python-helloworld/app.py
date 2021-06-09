from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status_response():
    status = {'result':'OK - healthy'}
    return jsonify(status)

@app.route("/metrics")
def metrics():
    metrics = {'UserCount':'40', 'UserCountActive':'23'}
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
