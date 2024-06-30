# traditional_crypto.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class TraditionalCrypto:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

    def decrypt(self, enc_data):
        enc_data = base64.b64decode(enc_data)
        nonce, tag, ciphertext = enc_data[:16], enc_data[16:32], enc_data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data
