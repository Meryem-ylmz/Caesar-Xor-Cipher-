# 🔐 Python Encryption Tool (Caesar & XOR)

This is a simple encryption-decryption CLI tool written in Python that supports:
- **Caesar Cipher** (with Turkish character support)
- **XOR Cipher** (with random key generation)
- File input/output for encrypted messages

---

## 🚀 Features

- Caesar encryption and decryption  
- XOR encryption with optional automatic key generation  
- File-based encrypted text storage and retrieval  
- Supports Turkish characters (ç, ğ, ö, ş, ü, ı)  
- Simple and interactive command-line interface

---

## 📦 Requirements

- Python 3.x

No additional libraries required.

---

## 🔧 Usage

Run the script using:

```bash
python main.py
```

You will be prompted to select an encryption method and follow the steps:

### Caesar Cipher Example:

```
1: Caesar Method
1: Encrypt
Please enter text: Merhaba dünya
Enter shift value: 3
Encrypted text: Phukgede güqçd
Encrypted text has been written to file (encrypted.txt)
```

### XOR Cipher Example with Random Key:

```
2: Xor Method
1: Encrypt
Please enter text: Hello World
Generate key automatically? (y/n): y
Automatically generated key: Ab3dLk...
Encrypted text has been written to file (xor_encrypted.txt)
```

---

## 📁 File Structure

```
.
├── caesar.py           # Caesar cipher logic
├── xor.py              # XOR cipher logic
├── main.py             # Main menu and program logic
├── encrypted.txt       # Output file for Caesar
├── xor_encrypted.txt   # Output file for XOR
├── Makefile            # Automation commands (run, clean, format)
└── README.md           # Project description and usage guide
```
---
