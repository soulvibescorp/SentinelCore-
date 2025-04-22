import json
import hashlib
import pyotp
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_totp(secret=None):
    if not secret:
        secret = pyotp.random_base32()
    return pyotp.TOTP(secret), secret

def verify_totp(secret, code):
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

