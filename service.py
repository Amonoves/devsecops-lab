import os
import ipaddress
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")

@app.route("/api/ping", methods=["GET"])
def system_ping():
    raw_host = request.args.get("host", "127.0.0.1")
    
    try:
        ip = ipaddress.ip_address(raw_host)
        validated_host = str(ip)
    except ValueError:
        return jsonify({"error": "Некоректний формат IP-адреси"}), 400

    cmd = ["ping", "-c", "1", validated_host]
    
    output = subprocess.run(cmd, capture_output=True, text=True, check=True)  # nosemgrep
    
    return jsonify({"result": output.stdout})

if __name__ == "__main__":
    app.run(port=5000)