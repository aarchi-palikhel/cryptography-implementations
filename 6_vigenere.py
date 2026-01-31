def vigenere_encrypt(text, key):
    key = key.upper()  # Convert the key to uppercase
    key_index = 0
    encrypted = ""
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(key[key_index % len(key)]) - 65  # Get the shift value for the key character
            base = 65 if char.isupper() else 97  # Determine if the character is uppercase or lowercase
            encrypted += chr((ord(char) - base + shift) % 26 + base)  # Encrypt the character
            key_index += 1  # Move to the next character in the key
        else:
            encrypted += char  # Non-alphabetic characters remain unchanged
    return encrypted

def vigenere_decrypt(text, key):
    key = key.upper()  # Convert the key to uppercase
    key_index = 0
    decrypted = ""
    for char in text:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(key[key_index % len(key)]) - 65  # Get the shift value for the key character
            base = 65 if char.isupper() else 97  # Determine if the character is uppercase or lowercase
            decrypted += chr((ord(char) - base - shift) % 26 + base)  # Decrypt the character
            key_index += 1  # Move to the next character in the key
        else:
            decrypted += char  # Non-alphabetic characters remain unchanged
    return decrypted

text = input("Enter the text to encrypt: ")
key = input("Enter the encryption key: ")
encrypted_text = vigenere_encrypt(text, key)
print("Vigenere Cipher Encrypted Text:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Vigenere Cipher Decrypted Text:", decrypted_text)
