import hashlib

# Function to calculate GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find a suitable public exponent e
def find_e(phi):
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e
    return None

# Function to calculate modular inverse
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

# Function for modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Function to hash the message using SHA-256 and reduce its size for RSA
def hash_message(message, modulus):
    # Create a SHA-256 hash of the message
    sha256 = hashlib.sha256()
    sha256.update(message.encode())  # Encode the message to bytes
    hash_value = int(sha256.hexdigest(), 16)  # Hash as an integer

    # Reduce the hash size for RSA
    return hash_value % modulus

# RSA encryption and decryption process
def rsa_encryption(p, q, message):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Automatically find a valid e
    e = find_e(phi)
    print(f"Automatically selected public exponent e: {e}")

    # Calculate the private key d
    d = mod_inverse(e, phi)

    # 1. Message Digest Creation
    hashed_message = hash_message(message, n)  # Use modulus to reduce hash size
    print(f"Hashed message (numeric): {hashed_message}")

    # 2. Signing with Private Key
    signed_message = mod_exp(hashed_message, d, n)
    print(f"Signed message (numeric): {signed_message}")

    # 3. Print the signature
    print(f"Digital Signature: {signed_message}")

    # 4. Verification with Public Key
    verified_hash = mod_exp(signed_message, e, n)
    print(f"Verified hash (numeric): {verified_hash}")

    # 5. Comparison
    if verified_hash == hashed_message:
        print("Verification successful: The message is authentic and has not been altered.")
    else:
        print("Verification failed: The message may have been altered.")

# Example usage
p = int(input("Enter a prime number p (larger prime): "))
q = int(input("Enter a prime number q (larger prime): "))
message = input("Enter the message to encrypt: ")

rsa_encryption(p, q, message)