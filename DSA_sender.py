import hashlib

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
        numeric_value += f"{numeric_index:02d}"

    return numeric_value

def hash_message(message):
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

def encrypt_in_chunks(message, d, n):
    block_size = len(str(n)) - 1
    chunks = [message[i:i + block_size] for i in range(0, len(message), block_size)]
    encrypted_chunks = [mod_exp(int(chunk), d, n) for chunk in chunks]

    encrypted_message = " ".join(map(str, encrypted_chunks))
    return encrypted_message

def rsa_encryption(p, q, message):
    n = p * q
    phi = (p - 1) * (q - 1)

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

    e = find_e(phi)
    d = mod_inverse(e, phi)
    hashed_message = hash_message(message)
    custom_hashed_message = hex_to_custom_decimal(hashed_message)
    original_message_numeric = message_to_numeric(message)
    combined_message = original_message_numeric + custom_hashed_message

    encrypted_message = encrypt_in_chunks(combined_message, d, n)
    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message, e, n

p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
message = input("Enter the message to encrypt: ")

encrypted_message, e, n = rsa_encryption(p, q, message)

print(f"Encrypted message: {encrypted_message}")
print(f"Public key (e, n): ({e}, {n})")