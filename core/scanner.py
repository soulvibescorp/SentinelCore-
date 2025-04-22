import os
import hashlib
import logging

LOG_FILE = "logs/sentinel.log"
THREAT_SIGNATURES = {
    "eicar": "44d88612fea8a8f36de82e1278abb02f",  # EICAR test string (standard fake virus signature)
    "testmalware": "5f4dcc3b5aa765d61d8327deb882cf99",  # MD5 of 'password'
}

def init_logger():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def hash_file(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing {file_path}: {e}")
        return None

def scan_directory(directory="."):
    init_logger()
    print("[🧪] Scanning directory for known threats...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = hash_file(path)
            if file_hash in THREAT_SIGNATURES.values():
                logging.warning(f"THREAT FOUND: {file} in {root}")
                print(f"[⚠️] THREAT FOUND in {path}")
            else:
                print(f"[✓] {file} - Clean")

def update_signatures(new_sigs):
    THREAT_SIGNATURES.update(new_sigs)
    print("[🔄] Signature DB updated.")

if __name__ == "__main__":
    scan_directory("test_samples")  # Replace with your test folder
