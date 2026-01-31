def affine_encrypt(text, a, b):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr(((a * (ord(char) - shift_base) + b) % 26) + shift_base)
        else:
            encrypted += char
    return encrypted

def affine_decrypt(text, a, b):
    # Find the modular inverse of a mod 26
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"The value 'a' ({a}) is not coprime with 26. Cannot decrypt.")
    
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted += chr(((a_inv * (ord(char) - shift_base - b)) % 26) + shift_base)
        else:
            decrypted += char
    return decrypted
def mod_inverse(a, m):
    # Find the modular inverse of a under modulo m using Extended Euclidean Algorithm
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
# User input for text and keys
text = input("Enter the text to encrypt: ")
a = int(input("Enter the value for 'a' (must be coprime with 26): "))
b = int(input("Enter the value for 'b': "))
# Perform encryption
encrypted_text = affine_encrypt(text, a, b)
print("Affine Encrypted Text:", encrypted_text)
# Perform decryption
decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Affine Decrypted Text:", decrypted_text)
