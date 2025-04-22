import hashlib

THREAT_SIGNATURES = [
    "d41d8cd98f00b204e9800998ecf8427e",  # Example hash
]

def scan_file(path):
    with open(path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    if file_hash in THREAT_SIGNATURES:
        return f"⚠ Threat detected in {path}"
    return f"✅ {path} is clean"

