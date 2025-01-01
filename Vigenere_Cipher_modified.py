alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Preprocess the plaintext by converting to uppercase and replacing spaces with filler
def preprocess_text(plaintext, filler):
    processed_text = ''
    for char in plaintext:
        if char != ' ':
            if char in alphabet_lower:
                index = alphabet_lower.index(char)
                processed_text += alphabet_upper[index]
            else:
                processed_text += char
        else:
            processed_text += filler
    return processed_text

# Adjust the key to the length of the plaintext using the autokey method
def adjust_key_for_encryption(plaintext, base_key):
    auto_key = base_key.upper()
    for char in plaintext:
        if char.isalpha():
            auto_key += char
    return auto_key[:len(plaintext)]

# Split the key into even and odd indexed parts
def split_key(key):
    even_key = ""
    odd_key = ""
    for i in range(len(key)):
        if i % 2 == 0:
            even_key += key[i]
        else:
            odd_key += key[i]
    return even_key, odd_key

# First encryption stage using split keys
def encryption_1(message, base_key, filler):
    plaintext = preprocess_text(message, filler)
    key = base_key.upper()
    even_key, odd_key = split_key(key)

    if len(plaintext) % 2 == 1:
        mid = len(plaintext) // 2 + 1
    else:
        mid = len(plaintext) // 2
    first_half = plaintext[:mid]
    second_half = plaintext[mid:]

    result = ''
    for i in range(len(first_half)):
        char = first_half[i]
        if char in alphabet_upper:
            key_char = even_key[i % len(even_key)]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c + k) % 26
            result += alphabet_upper[p]
        else:
            result += char

    for i in range(len(second_half)):
        char = second_half[i]
        if char in alphabet_upper:
            key_char = odd_key[i % len(odd_key)]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c + k) % 26
            result += alphabet_upper[p]
        else:
            result += char

    return result

# Second encryption stage using the autokey method
def encryption_stage2(ciphertext, base_key, filler):
    plaintext = preprocess_text(ciphertext, filler)
    auto_key = adjust_key_for_encryption(plaintext, base_key)

    result = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char in alphabet_upper:
            key_char = auto_key[i]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c + k) % 26
            result += alphabet_upper[p]
        else:
            result += char
    return result

# Adjust key for decryption based on already decrypted text
def adjust_key_for_decryption(ciphertext, base_key, decrypted_text):
    auto_key = base_key.upper() + decrypted_text
    return auto_key[:len(ciphertext)]

# Second decryption stage using autokey
def decryption_stage2(ciphertext, base_key, filler):
    auto_key = adjust_key_for_decryption(ciphertext, base_key, "")
    result = ''
    decrypted_text = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in alphabet_upper:
            key_char = auto_key[i]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c - k + 26) % 26
            decrypted_char = alphabet_upper[p]
            result += decrypted_char
            auto_key += decrypted_char  # Extend the key
        elif char == filler:
            result += ' '
        else:
            result += char
    return result

# First decryption stage using the split key
def decryption_stage1(ciphertext, base_key, filler):
    key = base_key.upper()
    even_key, odd_key = split_key(key)
    mid = len(ciphertext) // 2
    first_half = ciphertext[:mid]
    second_half = ciphertext[mid:]

    decrypted_text = ''
    for i in range(len(first_half)):
        char = first_half[i]
        if char in alphabet_upper:
            key_char = even_key[i % len(even_key)]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c - k + 26) % 26
            decrypted_text += alphabet_upper[p]
        else:
            decrypted_text += char

    for i in range(len(second_half)):
        char = second_half[i]
        if char in alphabet_upper:
            key_char = odd_key[i % len(odd_key)]
            c = alphabet_upper.index(char)
            k = alphabet_upper.index(key_char)
            p = (c - k + 26) % 26
            decrypted_text += alphabet_upper[p]
        else:
            decrypted_text += char

    return decrypted_text

# Complete encryption with both stages
def complete_encryption(message, base_key, filler):
    ciphertext_stage1 = encryption_1(message, base_key, filler)
    ciphertext_stage2 = encryption_stage2(ciphertext_stage1, base_key, filler)
    return ciphertext_stage2

# Complete decryption with both stages
def complete_decryption(ciphertext, base_key, filler):
    decrypted_text_1 = decryption_stage2(ciphertext, base_key, filler)
    decrypted_text = decryption_stage1(decrypted_text_1, base_key, filler)
    return decrypted_text

# Input and testing
message = input("Enter the plaintext: ")
base_key = "BATTLE"
filler = '*'

ciphertext = complete_encryption(message, base_key, filler)
print("Ciphertext: ", ciphertext)

decrypted_text = complete_decryption(ciphertext, base_key, filler)
print("Decrypted text: ", decrypted_text)