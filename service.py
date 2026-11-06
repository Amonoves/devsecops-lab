import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY_12345"

@app.route("/api/ping", methods=["GET"])
def system_ping():
    host = request.args.get("host", "127.0.0.1")
    

    command = f"ping -c 1 {host}"
    output = subprocess.check_output(command, shell=True, text=True)
    
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(port=5000)