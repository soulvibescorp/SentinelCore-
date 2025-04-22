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

