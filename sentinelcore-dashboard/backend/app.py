from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route("/logs/firewall")
def firewall_logs():
    logs = [
        "[PORT 8080] Intrusion Attempt Blocked",
        "[PORT 22] SSH Brute Force Blocked",
        "Status: Secured"
    ]
    return jsonify(logs)

@app.route("/logs/antivirus")
def antivirus_logs():
    logs = [
        f"Scan Complete: {random.randint(1,5)} threats removed",
        "DB Version: 2.8.1",
        "Next Scan: In 24hrs"
    ]
    return jsonify(logs)

@app.route("/logs/encryption")
def encryption_logs():
    logs = [
        "Folder /docs/vault locked 🔒",
        "Drive D:/Encrypted",
        "AES-256 encryption complete"
    ]
    return jsonify(logs)

@app.route("/logs/auth")
def auth_logs():
    logs = [
        "Login: Success (admin) [2FA verified]",
        "Access Blocked: Unknown device (3 attempts)"
    ]
    return jsonify(logs)

@app.route("/logs/ip")
def ip_logs():
    logs = [
        "Trace: 192.168.1.13 (Local Host)",
        "Blocked: Malicious IP 185.12.23.4 (Russia)"
    ]
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/logs/firewall")
def firewall_logs():
    return jsonify(read_firewall_log())

