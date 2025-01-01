import numpy as np
import random

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

def encryption_block(block_number, matrix, unit_digit, tens_digit):
    ciphernumber = np.dot(matrix, block_number) % 26
    ciphernumber[0] = (ciphernumber[0] + unit_digit) % 26
    ciphernumber[1] = (ciphernumber[1] + tens_digit) % 26
    return ciphernumber

def decryption_block(block_number, matrix, unit_digit, tens_digit):
    block_number[0] = (block_number[0] - unit_digit) % 26
    block_number[1] = (block_number[1] - tens_digit) % 26
    deciphernumber = np.dot(matrix, block_number) % 26
    return deciphernumber

def encryption(plaintext, matrix, unit_digit, tens_digit):
    n = matrix.shape[0]
    plain_number = text_to_number(plaintext)

    ciphertext = ''
    if len(plain_number) % n != 0:
        plain_number.extend([0] * (n - len(plain_number) % n))

    for i in range(0, len(plain_number), n):
        block_number = plain_number[i:i + n]
        ciphernumber = encryption_block(block_number, matrix, unit_digit, tens_digit)
        ciphertext += number_to_text(ciphernumber)
    return ciphertext

def decryption(ciphertext, matrix, unit_digit, tens_digit):
    inverse_matrix = matrix_inverse(matrix, 26)
    n = matrix.shape[0]
    cipher_number = text_to_number(ciphertext)

    plaintext = ''
    for i in range(0, len(cipher_number), n):
        block_number = cipher_number[i:i + n]
        plainnumber = decryption_block(block_number, inverse_matrix, unit_digit, tens_digit)
        plaintext += number_to_text(plainnumber)
    return plaintext

# Input plaintext and key
plaintext = input("Enter the plaintext: ")
print(f'Plaintext: {plaintext}')

key = input('Enter the key: ')
print(f'Key: {key}')

if len(key) <= 4:
    matrix = np.array(text_to_number(key)).reshape(2, 2)
else:
    matrix = np.array(text_to_number(key)).reshape(3, 3)

# Generate random two-digit key
random_key = random.randint(10, 99)
unit_digit = random_key % 10
tens_digit = random_key // 10
print(f'Random two-digit key: {random_key}')
print(f'Unit digit: {unit_digit}, Tens digit: {tens_digit}')

# Encryption process
ciphertext = encryption(plaintext, matrix, unit_digit, tens_digit)
print(f'Ciphertext: {ciphertext}')

# Decryption process
decrypted_text = decryption(ciphertext, matrix, unit_digit, tens_digit)
print(f'Decrypted text: {decrypted_text}')