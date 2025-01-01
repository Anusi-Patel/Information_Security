#Caesar Cipher
import random

def encrypt_caesar_cipher(text, key):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for char in text:
        if char in alphabet_upper:
            P = alphabet_upper.index(char)
            C = (P + key) % 26
            result += alphabet_upper[C]
        elif char in alphabet_lower:
            P = alphabet_lower.index(char)
            C = (P + key) % 26
            result += alphabet_lower[C]
        elif char.isspace():
            result += ""
    return result

def decrypt_caesar_cipher(text, key):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for char in text:
        if char in alphabet_upper:
            C = alphabet_upper.index(char)
            P = (C - key) % 26
            result += alphabet_upper[P]
        elif char in alphabet_lower:
            C = alphabet_lower.index(char)
            P = (C - key) % 26
            result += alphabet_lower[P]
        elif char.isspace():
            result += ""

    return result

plaintext = input("Enter the text to be encrypted: ")
key = random.randint(1, 25)

encrypted_text = encrypt_caesar_cipher(plaintext, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_caesar_cipher(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")