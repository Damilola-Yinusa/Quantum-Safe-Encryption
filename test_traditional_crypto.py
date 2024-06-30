# tests/test_traditional_crypto.py
import unittest
from traditional_crypto import TraditionalCrypto

class TestTraditionalCrypto(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = b'Sixteen byte key'
        crypto = TraditionalCrypto(key)
        data = b"Test data for encryption"
        enc_data = crypto.encrypt(data)
        dec_data = crypto.decrypt(enc_data)
        self.assertEqual(data, dec_data)

if __name__ == '__main__':
    unittest.main()
