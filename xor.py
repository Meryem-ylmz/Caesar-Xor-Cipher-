def decimal_to_binary(n):
    binary = ""
    while n > 0:
        bit = n % 2
        binary = str(bit) + binary
        n = n // 2
    while len(binary) < 8:
        binary = "0" + binary
    return binary

def binary_to_decimal(binary_str):
    decimal = 0
    uzunluk = len(binary_str)

    for i in range(uzunluk):
        bit = int(binary_str[uzunluk - 1 - i])
        decimal += bit * (2 ** i)
    return decimal


def xor_binary_strings(bin1, bin2):
    xor_result = ""
    for i in range(len(bin1)):
        bit1 = bin1[i]
        bit2 = bin2[i]

        if bit1 == bit2:
            xor_result += "0"
        else:
            xor_result += "1"
    return xor_result

def xor_encrypt(text, key_char):
    encrypted_text = ""
    key_index = 0
    for char in text:
        key_binary = decimal_to_binary(ord(key_char[key_index]))  
        char_binary = decimal_to_binary(ord(char))  
        xor_result = xor_binary_strings(char_binary, key_binary)
        xor_decimal = binary_to_decimal(xor_result)
        encrypted_char = chr(xor_decimal)
        encrypted_text += encrypted_char
        key_index = (key_index + 1) % len(key_char)  
    
    return encrypted_text

def xor_decrypt(encrypted_text, key_char):
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        key_binary = decimal_to_binary(ord(key_char[key_index]))  
        char_binary = decimal_to_binary(ord(char))  
        xor_result = xor_binary_strings(char_binary, key_binary)
        xor_decimal = binary_to_decimal(xor_result)
        decrypted_char = chr(xor_decimal)
        decrypted_text += decrypted_char
        key_index = (key_index + 1) % len(key_char)  
    
    return decrypted_text