#PlayFair Cipher
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

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def encrypt(plaintext, key):
    matrix = create_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")
    prepared_text = ""

    i = 0
    while i < len(plaintext):
        if plaintext[i] < 'A' or plaintext[i] > 'Z':
            i += 1
            continue
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            prepared_text += plaintext[i] + 'X'
            i += 1
        else:
            if i + 1 < len(plaintext):
                prepared_text += plaintext[i] + plaintext[i + 1]
                i += 2
            else:
                prepared_text += plaintext[i] + 'X'
                i += 1

    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
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

    return ciphertext

def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    prepared_text = ""

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i + 1])

        if row1 == row2:  # Same row
            prepared_text += matrix[row1][(col1 - 1) % 5]
            prepared_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            prepared_text += matrix[(row1 - 1) % 5][col1]
            prepared_text += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            prepared_text += matrix[row1][col2]
            prepared_text += matrix[row2][col1]


    return prepared_text

key = "BATTLE"
plaintext = input("Enter the plain text: ")
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)