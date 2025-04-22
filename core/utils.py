import os
import json
import hashlib
import logging
from datetime import datetime

LOG_FILE = "logs/sentinel.log"
CONFIG_FILE = "config/config.json"

# ----------------------------
# 🧠 CONFIGURATION LOADER
# ----------------------------
def load_config():
    if not os.path.exists(CONFIG_FILE):
        logging.warning("[⚠️] Config not found. Using defaults.")
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config_data):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)

# ----------------------------
# 🪪 HASHING TOOLS (file/digest)
# ----------------------------
def hash_string(text, algo="sha256"):
    if algo == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm")

def hash_file(file_path, algo="sha256"):
    h = hashlib.new(algo)
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        log_event(f"Error hashing file {file_path}: {str(e)}", level="error")
        return None

# ----------------------------
# 📓 LOGGING SYSTEM
# ----------------------------
def init_logger():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_event(message, level="info"):
    init_logger()
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    formatted = f"[{timestamp}] {message}"
    if level == "info":
        logging.info(formatted)
    elif level == "warn":
        logging.warning(formatted)
    elif level == "error":
        logging.error(formatted)
    print(formatted)

# ----------------------------
# ✅ TEST
# ----------------------------
if __name__ == "__main__":
    init_logger()
    log_event("SentinelCore utilities loaded.")
    config = load_config()
    print("Current Config:", config)
    print("Hash test (sha256):", hash_string("SentinelCore"))

