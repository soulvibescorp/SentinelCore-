from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def decrypt_data(blob, key):
    nonce = blob[:16]
    tag = blob[16:32]
    ciphertext = blob[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

def encrypt_file(file_path, output_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = encrypt_data(data, key)
    with open(output_path, 'wb') as f:
        f.write(encrypted)

def decrypt_file(file_path, output_path, key):
    with open(file_path, 'rb') as f:
        decrypted = decrypt_data(f.read(), key)
    with open(output_path, 'wb') as f:
        f.write(decrypted)


import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY_FILE = "storage/master.key"

def generate_key():
    key = get_random_bytes(32)  # AES-256
    os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(input_path, output_path):
    key = load_key()
    cipher = AES.new(key, AES.MODE_GCM)
    with open(input_path, "rb") as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    with open(output_path, "wb") as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

def decrypt_file(input_path, output_path):
    key = load_key()
    with open(input_path, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(output_path, "wb") as f:
        f.write(plaintext)
