# tests/test_lattice_based_crypto.py
import unittest
from lattice_based_crypto import LatticeBasedCrypto

class TestLatticeBasedCrypto(unittest.TestCase):
    def setUp(self):
        self.crypto = LatticeBasedCrypto()

    def test_encrypt_decrypt(self):
        data = b"Test data for encryption"
        enc_data = self.crypto.encrypt(data)
        dec_data = self.crypto.decrypt(enc_data)
        self.assertEqual(data, dec_data)

if __name__ == '__main__':
    unittest.main()
