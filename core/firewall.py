import json

def load_rules():
    with open('config/config.json') as f:
        return json.load(f)['firewall']['allowed_ports']

def is_allowed(port):
    return port in load_rules()

def run_check(port):
    return f"✅ Port {port} allowed" if is_allowed(port) else f"❌ Port {port} blocked"
