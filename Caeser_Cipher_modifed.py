import random

def encrypt_caesar_cipher(text, key):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char in alphabet_upper:
            C = alphabet_upper.index(char)
            K = int(key[i ** 2 % len(key)])
            P = (C + K) % 26
            result += alphabet_upper[P]
        elif char in alphabet_lower:
            C = alphabet_lower.index(char)
            K = int(key[i ** 2 % len(key)])
            P = (C + K) % 26
            result += alphabet_upper[P]
        else:
            result += char

    return result

def decrypt_caesar_cipher(text, key):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char in alphabet_upper:
            C = alphabet_upper.index(char)
            K = int(key[i ** 2 % len(key)])
            P = (C - K) % 26
            result += alphabet_upper[P]
        elif char in alphabet_lower:
            C = alphabet_lower.index(char)
            K = int(key[i ** 2 % len(key)])
            P = (C - K) % 26
            result += alphabet_lower[P]
        else:
            continue

    return result

def generate_random_key(length):
    nums = '0123456789'
    key = ""
    for _ in range(length):
        key += random.choice(nums)
    return key

# Get user input
text = input("Enter the text to encrypt: ")
key = generate_random_key(len(text.replace(" ", "")))
encrypted_text = encrypt_caesar_cipher(text, key)
decrypted_text = decrypt_caesar_cipher(encrypted_text, key)

print("Original Text:", text)
print("Key:", key)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)