import numpy as np

def text_to_number(text):
    return [ord(char) - ord('A') for char in text.upper()]

def number_to_text(number):
    return ''.join(chr(num + ord('A')) for num in number)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def matrix_determinant(matrix):
    if matrix.shape == (2, 2):
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    elif matrix.shape == (3, 3):
        return (matrix[0, 0] * (matrix[1, 1] * matrix[2, 2] - matrix[1, 2] * matrix[2, 1]) -
                matrix[0, 1] * (matrix[1, 0] * matrix[2, 2] - matrix[1, 2] * matrix[2, 0]) +
                matrix[0, 2] * (matrix[1, 0] * matrix[2, 1] - matrix[1, 1] * matrix[2, 0]))
    else:
        raise ValueError("Matrix should be either 2x2 or 3x3.")

def matrix_inverse(matrix, modulus):
    det = matrix_determinant(matrix) % modulus
    if det == 0:  # Check if determinant is zero
        raise ValueError("Matrix is singular and cannot be inverted.")
    det_inv = mod_inverse(det, modulus)
    if matrix.shape == (2, 2):
        inverse_matrix = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])
    elif matrix.shape == (3, 3):
        cofactors = np.zeros(matrix.shape, dtype=int)
        for i in range(3):
            for j in range(3):
                sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                sign = (-1) ** (i + j)
                cofactors[i, j] = sign * matrix_determinant(sub_matrix)
        inverse_matrix = np.transpose(cofactors)
    return (det_inv * inverse_matrix) % modulus

def encryption_block(block_number, matrix):
    ciphernumber = np.dot(matrix, block_number) % 26
    return ciphernumber

def decryption_block(block_number, matrix):
    deciphernumber = np.dot(matrix, block_number) % 26
    return deciphernumber

def encryption(plaintext, matrix):
    n = matrix.shape[0]
    plain_number = text_to_number(plaintext)

    ciphertext = ''
    if len(plain_number) % n != 0:
        plain_number.extend([0] * (n - len(plain_number) % n))  # Padding with 0

    for i in range(0, len(plain_number), n):
        block_number = plain_number[i:i + n]
        ciphernumber = encryption_block(block_number, matrix)
        ciphertext += number_to_text(ciphernumber)
    return ciphertext

def decryption(ciphertext, matrix):
    inverse_matrix = matrix_inverse(matrix, 26)
    n = matrix.shape[0]
    cipher_number = text_to_number(ciphertext)

    plaintext = ''
    for i in range(0, len(cipher_number), n):
        block_number = cipher_number[i:i + n]
        plainnumber = decryption_block(block_number, inverse_matrix)
        plaintext += number_to_text(plainnumber)
    return plaintext.strip()  # Remove any padding added during encryption

def main():
    # Input plaintext and key
    plaintext = input("Enter the plaintext: ").upper()
    print(f'Plaintext: {plaintext}')

    key = input('Enter the key: ').upper()
    print(f'Key: {key}')

    # Generate matrix from the key
    if len(key) == 4:
        matrix = np.array(text_to_number(key)).reshape(2, 2)
    elif len(key) == 9:
        matrix = np.array(text_to_number(key)).reshape(3, 3)
    else:
        raise ValueError("Key length must be either 4 (2x2 matrix) or 9 (3x3 matrix)")

    # Encryption process
    ciphertext = encryption(plaintext, matrix)
    print(f'Ciphertext: {ciphertext}')

    # Decryption process
    decrypted_text = decryption(ciphertext, matrix)
    print(f'Decrypted text: {decrypted_text}')

if __name__ == "__main__":
    main()