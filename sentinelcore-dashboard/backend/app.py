@app.route("/logs/firewall")
def firewall_logs():
    return jsonify(read_firewall_log())

