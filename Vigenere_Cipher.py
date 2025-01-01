alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def preprocess_text(plaintext, filler):
    processed_text = ''
    for char in plaintext:
        if char != ' ':
            if char in alphabet_lower:
                index = alphabet_lower.index(char)
                processed_text += alphabet_upper[index]
            else:
                processed_text += char
        else:
            processed_text += filler
    return processed_text

def adjust_key(plaintext, keys):
    plain_length = len(plaintext)
    key_length = len(keys)
    while key_length != plain_length:
        if key_length > plain_length:
            keys = keys[:plain_length]
        elif key_length < plain_length:
            keys = (keys * (plain_length // key_length + 1))[:plain_length]
        key_length = len(keys)
    return keys

def encryption(message, keys, filler):
    plaintext = preprocess_text(message, filler)
    keys = adjust_key(plaintext, keys)
    result = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        key = keys[i]
        if char in alphabet_upper:
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key)
            p = (c + k) % 26
            result += alphabet_upper[p]
        else:
            result += char
    return result

def decryption(ciphertext, keys, filler):
    keys = adjust_key(ciphertext, keys)
    result = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key = keys[i]
        if char in alphabet_upper:
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key)
            p = (c - k + 26) % 26
            result += alphabet_upper[p]
        elif char == filler:
            result += ' '
        else:
            result += char
    return result

message = input("Enter the plaintext: ")
keys = input('Key: ')
filler = '*'
ciphertext = encryption(message, keys, filler)
print("Ciphertext:", ciphertext)

decrypted_text = decryption(ciphertext, keys, filler)
print("Decrypted Text:", decrypted_text)