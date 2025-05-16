from caesar import encrypt_caesar, decrypt_caesar
from xor import xor_encrypt, xor_decrypt
import random
import string

def generate_random_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

print("Select encryption method.\n")
choice = int(input("1: Caesar Method\n2: Xor Method\n"))
if choice == 1:
    print("Do you want to encrypt or decrypt?\n")
    selection = int(input("1: Encrypt\n2: Decrypt\n"))
    if selection == 1:
        text = input("Please enter text: \n")
        shift = int(input("Enter shift value: \n"))
        encrypted_text = encrypt_caesar(text, shift)
        print(f"Encrypted text: {encrypted_text}")

        with open("encrypted.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_text)
        print("Encrypted text has been written to file (encrypted.txt)")

        with open("encrypted.txt", "r", encoding="utf-8") as file:
            encrypted_from_file = file.read()

        decrypted = decrypt_caesar(encrypted_from_file, shift)
        print(f"Text read from file: {encrypted_from_file}")
        print(f"Decrypted text (verification): {decrypted}")

    elif selection == 2:
        text = input("Please enter text: \n")
        shift = int(input("Enter shift value: \n"))
        decrypted_text = decrypt_caesar(text, shift)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid selection. Please make a valid choice.\n")

elif choice == 2:
    print("Do you want to encrypt or decrypt?\n")
    selection = int(input("1: Encrypt\n2: Decrypt\n"))
    if selection == 1:
        text = input("Please enter text: \n")

        auto_key = input("Generate key automatically? (y/n): ").lower()
        if auto_key == "y":
            key_char = generate_random_key(len(text))
            print(f"Automatically generated key: {key_char}")
        else:
            key_char = input("Enter the key word\n")

        encrypted_text = xor_encrypt(text, key_char)
        print(f"Encrypted text: {encrypted_text}")

        with open("xor_encrypted.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_text)
        print("Encrypted text has been written to file (xor_encrypted.txt)")

        with open("xor_encrypted.txt", "r", encoding="utf-8") as file:
            encrypted_from_file = file.read()

        decrypted = xor_decrypt(encrypted_from_file, key_char)
        print(f"Text read from file: {encrypted_from_file}")
        print(f"Decrypted text (verification): {decrypted}")

    elif selection == 2:
        encrypted_text = input("Please enter encrypted text: \n")
        key_char = input("Enter the key word\n")
        decrypted_text = xor_decrypt(encrypted_text, key_char)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid selection. Please make a valid choice.\n")
else:
    print("Invalid selection. Please make a valid choice.\n")