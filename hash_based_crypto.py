# hash_based_crypto.py
from sphincs import Sphincs  # Assume you have implemented or installed a library for SPHINCS+
import base64

class HashBasedCrypto:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, data):
        sphincs = Sphincs()
        ciphertext = sphincs.sign(data, self.private_key)
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, enc_data):
        enc_data = base64.b64decode(enc_data)
        sphincs = Sphincs()
        data = sphincs.verify(enc_data, self.public_key)
        return data
