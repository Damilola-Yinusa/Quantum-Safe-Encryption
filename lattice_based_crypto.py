# lattice_based_crypto.py
from pqcrypto.kem import kyber512
import base64

class LatticeBasedCrypto:
    def __init__(self):
        self.public_key, self.private_key = kyber512.generate_keypair()

    def encrypt(self, data):
        ciphertext, _ = kyber512.encrypt(self.public_key, data)
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, enc_data):
        enc_data = base64.b64decode(enc_data)
        data = kyber512.decrypt(self.private_key, enc_data)
        return data
