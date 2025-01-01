def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def numeric_to_message(numeric_value):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = []
    temp_value = str(numeric_value)

    while len(temp_value) >= 2:
        pair = temp_value[:2]
        numeric_index = int(pair)
        chars.append(alphabet[numeric_index])
        temp_value = temp_value[2:]

    return ''.join(chars)

def decrypt_in_chunks(encrypted_message, e, n):
    encrypted_chunks = list(map(int, encrypted_message.split()))
    decrypted_chunks = [str(mod_exp(chunk, e, n)) for chunk in encrypted_chunks]
    return decrypted_chunks

def hash_message(message):
    import hashlib
    sha256 = hashlib.sha256()
    sha256.update(message.encode())
    return sha256.hexdigest()

def hex_to_custom_decimal(hex_message):
    decimal_message = ""
    for char in hex_message:
        if char.isdigit():
            decimal_message += char
        else:
            decimal_message += str(ord(char) - ord('a') + 1)
    return decimal_message

def rsa_decryption(encrypted_message, e, n):
    decrypted_chunks = decrypt_in_chunks(encrypted_message, e, n)
    decrypted_message = ''.join(decrypted_chunks)

    hashed_length = 64
    decrypted_numeric_message = decrypted_message[:-hashed_length]
    decrypted_hashed_message = decrypted_message[-hashed_length:]

    decrypted_message_alphabetic = numeric_to_message(decrypted_numeric_message)
    expected_hashed_message = hex_to_custom_decimal(hash_message(decrypted_message_alphabetic))

    if expected_hashed_message == decrypted_hashed_message:
        print("Verification successful: The message is authentic and has not been altered.")
    else:
        print("Verification failed: The message may have been altered.")

encrypted_message = input("Enter the encrypted message (space-separated): ")
e = int(input("Enter the public key exponent e: "))
n = int(input("Enter the modulus n: "))

rsa_decryption(encrypted_message, e, n)