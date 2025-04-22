import sqlite3
import os
import json
import logging
import base64
import pyotp
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

VAULT_PATH = "storage/vault.db"
LOG_FILE = "logs/sentinel.log"

# Master key for demo (replace with real key storage)
MASTER_KEY = AESGCM.generate_key(bit_length=256)

def init_logger():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def init_vault():
    os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)
    conn = sqlite3.connect(VAULT_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (
                    service TEXT PRIMARY KEY,
                    username TEXT,
                    nonce TEXT,
                    encrypted_password TEXT
                )''')
    conn.commit()
    conn.close()

def encrypt_password(password):
    aesgcm = AESGCM(MASTER_KEY)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, password.encode(), None)
    return base64.b64encode(nonce).decode(), base64.b64encode(encrypted).decode()

def decrypt_password(nonce_b64, encrypted_b64):
    nonce = base64.b64decode(nonce_b64)
    encrypted = base64.b64decode(encrypted_b64)
    aesgcm = AESGCM(MASTER_KEY)
    decrypted = aesgcm.decrypt(nonce, encrypted, None)
    return decrypted.decode()

def store_password(service, username, password):
    init_vault()
    nonce, encrypted = encrypt_password(password)
    conn = sqlite3.connect(VAULT_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO passwords VALUES (?, ?, ?, ?)",
              (service, username, nonce, encrypted))
    conn.commit()
    conn.close()
    logging.info(f"Stored password for {service}")

def retrieve_password(service):
    conn = sqlite3.connect(VAULT_PATH)
    c = conn.cursor()
    c.execute("SELECT username, nonce, encrypted_password FROM passwords WHERE service=?", (service,))
    row = c.fetchone()
    conn.close()
    if row:
        username, nonce, encrypted = row
        password = decrypt_password(nonce, encrypted)
        return username, password
    else:
        return None

# -----------------------------
# 🔐 Two-Factor Auth (TOTP)
# -----------------------------
def create_2fa_secret():
    secret = pyotp.random_base32()
    print(f"[QR] Set this up in Google Authenticator: {pyotp.totp.TOTP(secret).provisioning_uri('SentinelCore', issuer_name='SentinelCore Security')}")
    return secret

def verify_2fa_token(secret, token):
    totp = pyotp.TOTP(secret)
    return totp.verify(token)

# -----------------------------
# 🔗 Duo Auth (placeholder)
# -----------------------------
def simulate_duo_auth(username):
    print(f"[DUO] Simulating Duo push for {username}...")
    print("[✅] Authenticated via Duo (mocked)")

# -----------------------------
# 🔁 Demo use
# -----------------------------
if __name__ == "__main__":
    init_logger()
    print("🔐 SentinelCore Auth Vault")
    store_password("example.com", "admin", "SuperSecret123")
    u, p = retrieve_password("example.com")
    print(f"Retrieved: {u} / {p}")

    secret = create_2fa_secret()
    token = input("Enter your current 2FA token: ")
    if verify_2fa_token(secret, token):
        print("✅ 2FA success")
    else:
        print("❌ Invalid 2FA token")

    simulate_duo_auth("admin_user")
