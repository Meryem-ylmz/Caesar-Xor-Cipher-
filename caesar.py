def encrypt_caesar(text, shift):
    turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    encrypted_text = ''

    for char in text:
        if char.lower() in turkish_alphabet:
            is_upper = char.isupper()
            index = turkish_alphabet.index(char.lower())
            new_index = (index + shift) % len(turkish_alphabet)
            new_char = turkish_alphabet[new_index]
            encrypted_text += new_char.upper() if is_upper else new_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)