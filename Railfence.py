alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def preprocess_text(plaintext):
    processed_text = ''
    for char in plaintext:
        if char != ' ':
            if char in alphabet_lower:
                index = 0
                for i in range(len(alphabet_lower)):
                    if alphabet_lower[i] == char:
                        index = i
                        break
                processed_text += alphabet_upper[index]
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
    index = 0
    for i in range(len(ciphertext)):
        matrix[row][i] = '*'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
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

plaintext = input("Enter the plaintext: ")
key = 3
processed_plaintext = preprocess_text(plaintext)
encrypted = rail_fence_encrypt(processed_plaintext, key)
print(f"Encrypted: {encrypted}")

decrypted = rail_fence_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")