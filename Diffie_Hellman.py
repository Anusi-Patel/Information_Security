import random

def is_generator(g, p):
    required_set = set(num for num in range(1, p))
    generated_set = set((g ** power) % p for power in range(1, p))
    return required_set == generated_set

def find_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g
    return None

def diffie_hellman(p, g):
    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)

    A = (g ** a) % p
    B = (g ** b) % p

    shared_secret_Alice = (B ** a) % p
    shared_secret_Bob = (A ** b) % p

    return shared_secret_Alice, shared_secret_Bob

p = int(input("Enter a prime number (p): "))
g = find_generator(p)

if g:
    print(f"The generator for {p} is: {g}")

    shared_secret_Alice, shared_secret_Bob = diffie_hellman(p, g)

    print(f"Alice's shared secret: {shared_secret_Alice}")
    print(f"Bob's shared secret: {shared_secret_Bob}")

    if shared_secret_Alice == shared_secret_Bob:
        print("Shared secrets match! Key exchange successful.")
    else:
        print("Shared secrets do not match! Key exchange failed.")
else:
    print(f"Could not find a generator for {p}.")