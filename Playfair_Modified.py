import random

def create_matrices(key):
    def create_matrix(key):
        matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for char in key:
            if char not in matrix and char in alphabet:
                matrix.append(char)

        for char in alphabet:
            if char not in matrix:
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    # Split the key into two parts
    if len(key) % 2 == 1:
        mid = len(key) // 2 + 1
    else:
        mid = len(key) // 2
    key1 = key[:mid]
    key2 = key[mid:]

    matrix1 = create_matrix(key1)
    matrix2 = create_matrix(key2)
    return matrix1, matrix2

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def encrypt(plaintext, key):
    matrix1, matrix2 = create_matrices(key)
    plaintext = plaintext.upper().replace("J", "I")

    # Remove all spaces and non-alphabetic characters
    prepared_text = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':
            prepared_text += char

    i = 0
    while i < len(prepared_text):
        if i + 1 < len(prepared_text) and prepared_text[i] == prepared_text[i + 1]:
            prepared_text = prepared_text[:i+1] + 'X' + prepared_text[i+1:]
        i += 2

    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'

    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        matrix = matrix1 if (i // 2) % 2 == 0 else matrix2
        row1, col1 = find_position(matrix, prepared_text[i])
        row2, col2 = find_position(matrix, prepared_text[i + 1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    # Generate and append a random character
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    random_char = alphabet[random.randint(0, len(alphabet) - 1)]
    ciphertext += random_char

    return ciphertext

def decrypt(ciphertext, key):
    matrix1, matrix2 = create_matrices(key)
    ciphertext = ciphertext[:-1]  # Remove random character
    prepared_text = ""

    for i in range(0, len(ciphertext), 2):
        matrix = matrix1 if (i // 2) % 2 == 0 else matrix2
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i + 1])

        if row1 == row2:
            prepared_text += matrix[row1][(col1 - 1) % 5]
            prepared_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            prepared_text += matrix[(row1 - 1) % 5][col1]
            prepared_text += matrix[(row2 - 1) % 5][col2]
        else:
            prepared_text += matrix[row1][col2]
            prepared_text += matrix[row2][col1]

    return prepared_text

key = "BATTLE"
plaintext = input("Enter the plain text: ")

# Modify the plaintext to remove spaces and any non-alphabetic characters
plaintext = "".join([char for char in plaintext if char.isalpha()])

ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)