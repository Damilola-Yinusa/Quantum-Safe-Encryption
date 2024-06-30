# app.py
import argparse
from traditional_crypto import TraditionalCrypto
from lattice_based_crypto import LatticeBasedCrypto
from hash_based_crypto import HashBasedCrypto

def main():
    parser = argparse.ArgumentParser(description='Quantum-Safe Encryption Application')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode: encrypt or decrypt')
    parser.add_argument('method', choices=['traditional', 'lattice', 'hash'], help='Encryption method')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('output_file', help='Output file')
    args = parser.parse_args()

    with open(args.input_file, 'rb') as f:
        data = f.read()

    if args.method == 'traditional':
        key = b'Sixteen byte key'
        crypto = TraditionalCrypto(key)
    elif args.method == 'lattice':
        crypto = LatticeBasedCrypto()
    elif args.method == 'hash':
        public_key, private_key = b'public_key', b'private_key'  # Replace with actual keys
        crypto = HashBasedCrypto(public_key, private_key)

    if args.mode == 'encrypt':
        result = crypto.encrypt(data)
    elif args.mode == 'decrypt':
        result = crypto.decrypt(data)

    with open(args.output_file, 'wb') as f:
        f.write(result.encode() if args.mode == 'encrypt' else result)

if __name__ == '__main__':
    main()
