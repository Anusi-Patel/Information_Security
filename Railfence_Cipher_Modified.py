alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

def preprocess_text(plaintext):
    processed_text = ''
    for char in plaintext:
        if char != ' ':
            if 'a' <= char <= 'z':
                for i in range(len(alphabet_lower)):
                    if alphabet_lower[i] == char:
                        processed_text += alphabet_upper[i]
                        break
            else:
                processed_text += char
    return processed_text

def rail_fence_encrypt(plaintext, key):
    matrix = [['' for _ in range(len(plaintext))] for _ in range(key)]
    row = 0
    direction = 1
    for i in range(len(plaintext)):
        matrix[row][i] = plaintext[i]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    ciphertext = ''
    for r in range(key):
        for c in range(len(plaintext)):
            if matrix[r][c] != '':
                ciphertext += matrix[r][c]
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    row = 0
    direction = 1

    for i in range(len(ciphertext)):
        matrix[row][i] = '*'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    index = 0
    for r in range(key):
        for c in range(len(ciphertext)):
            if matrix[r][c] == '*':
                matrix[r][c] = ciphertext[index]
                index += 1
    plaintext = ''
    row = 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext += matrix[row][i]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return plaintext

def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            for i in range(len(alphabet_upper)):
                if alphabet_upper[i] == char:
                    new_position = (i + key) % 26
                    result += alphabet_upper[new_position]
                    break
    return result

def caesar_decrypt(text, key):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            for i in range(len(alphabet_upper)):
                if alphabet_upper[i] == char:
                    new_position = (i - key + 26) % 26
                    result += alphabet_upper[new_position]
                    break
    return result

def modified_cipher_encrypt(plaintext, rail_key1, caesar_key, rail_key2):
    processed_plaintext = preprocess_text(plaintext)
    step1 = rail_fence_encrypt(processed_plaintext, rail_key1)
    step2 = caesar_encrypt(step1, caesar_key)
    final_encryption = rail_fence_encrypt(step2, rail_key2)
    return final_encryption

def modified_cipher_decrypt(ciphertext, rail_key1, caesar_key, rail_key2):
    step1 = rail_fence_decrypt(ciphertext, rail_key2)
    step2 = caesar_decrypt(step1, caesar_key)
    final_decryption = rail_fence_decrypt(step2, rail_key1)
    return final_decryption

# User input
plaintext = input("Enter the plaintext: ")
rail_key1 = 3
rail_key2 = 3
caesar_key = 4

# Encrypt
encrypted_text = modified_cipher_encrypt(plaintext, rail_key1, caesar_key, rail_key2)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt
decrypted_text = modified_cipher_decrypt(encrypted_text, rail_key1, caesar_key, rail_key2)
print(f"Decrypted Text: {decrypted_text}")