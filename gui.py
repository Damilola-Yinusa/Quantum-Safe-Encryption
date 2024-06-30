# gui.py
import tkinter as tk
from tkinter import filedialog
from traditional_crypto import TraditionalCrypto
from lattice_based_crypto import LatticeBasedCrypto
from hash_based_crypto import HashBasedCrypto

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum-Safe Encryption")
        self.create_widgets()

    def create_widgets(self):
        self.method_var = tk.StringVar(value="traditional")
        tk.Label(self.root, text="Select Encryption Method:").pack()
        tk.Radiobutton(self.root, text="Traditional", variable=self.method_var, value="traditional").pack()
        tk.Radiobutton(self.root, text="Lattice-Based", variable=self.method_var, value="lattice").pack()
        tk.Radiobutton(self.root, text="Hash-Based", variable=self.method_var, value="hash").pack()

        tk.Button(self.root, text="Select File", command=self.select_file).pack()
        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack()

        tk.Button(self.root, text="Encrypt", command=self.encrypt_file).pack()
        tk.Button(self.root, text="Decrypt", command=self.decrypt_file).pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def select_file(self):
        self.filepath = filedialog.askopenfilename()
        self.file_label.config(text=self.filepath)

    def encrypt_file(self):
        method = self.method_var.get()
        with open(self.filepath, 'rb') as f:
            data = f.read()
        
        if method == "traditional":
            key = b'Sixteen byte key'
            crypto = TraditionalCrypto(key)
        elif method == "lattice":
            crypto = LatticeBasedCrypto()
        elif method == "hash":
            public_key, private_key = b'public_key', b'private_key'  # Replace with actual keys
            crypto = HashBasedCrypto(public_key, private_key)
        
        enc_data = crypto.encrypt(data)
        self.save_file(enc_data)

    def decrypt_file(self):
        method = self.method_var.get()
        with open(self.filepath, 'rb') as f:
            enc_data = f.read()
        
        if method == "traditional":
            key = b'Sixteen byte key'
            crypto = TraditionalCrypto(key)
        elif method == "lattice":
            crypto = LatticeBasedCrypto()
        elif method == "hash":
            public_key, private_key = b'public_key', b'private_key'  # Replace with actual keys
            crypto = HashBasedCrypto(public_key, private_key)
        
        data = crypto.decrypt(enc_data)
        self.save_file(data)

    def save_file(self, data):
        save_path = filedialog.asksaveasfilename()
        with open(save_path, 'wb') as f:
            f.write(data)
        self.result_label.config(text="Operation completed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
