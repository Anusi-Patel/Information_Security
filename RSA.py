def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e
    return None

def mod_inverse(e, phi):
    t1, t2 = 0, 1
    r1, r2 = phi, e
    while r2 > 0:
        quotient = r1 // r2
        r1, r2 = r2, r1 - quotient * r2
        t1, t2 = t2, t1 - quotient * t2

    if r1 == 1:
        return t1 % phi
    return None

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def message_to_numeric(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeric_value = ""

    for char in message:
        numeric_index = alphabet.index(char)
        numeric_value += f"{numeric_index:02d}"  # Encode each letter as two digits

    return numeric_value  # Return as string

def numeric_to_message(numeric_value):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = []
    temp_value = str(numeric_value)  # Ensure input is a string

    # Process two-character blocks
    while len(temp_value) >= 2:
        pair = temp_value[:2]  # Take the first two characters
        numeric_index = int(pair)
        chars.append(alphabet[numeric_index])  # Append corresponding letter
        temp_value = temp_value[2:]  # Remove processed characters

    return ''.join(chars)

def rsa_encryption(p, q, message):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = find_e(phi)
    print(f"Automatically selected public exponent e: {e}")

    numeric_message = message_to_numeric(message)
    print(f"Numeric equivalent of message: {numeric_message}")

    # Convert numeric message to integer for encryption
    numeric_message_int = int(numeric_message)
    d = mod_inverse(e, phi)
    print(d)
    encrypted_message = mod_exp(numeric_message_int, e, n)
    print(f"Encrypted message (numeric): {encrypted_message}")

    decrypted_message = mod_exp(encrypted_message, d, n)
    print(f"Decrypted message (numeric): {decrypted_message}")

    # Convert back to string and decode message
    decrypted_message_str = f"{decrypted_message:0{len(numeric_message)}d}"  # Preserve leading zeros
    original_message = numeric_to_message(decrypted_message_str)
    print(f"Original message: {original_message}")

p = int(input("Enter a prime number p (larger prime): "))
q = int(input("Enter a prime number q (larger prime): "))
message = input("Enter the message to encrypt: ")

rsa_encryption(p, q, message)