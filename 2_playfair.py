def playfair_cipher(text, key, mode='encrypt'):
    key_square = create_key_square(key)
    processed_text = preprocess_text(text)
    if mode == 'encrypt':
        return encrypt_playfair(processed_text, key_square)
    else:
        return decrypt_playfair(processed_text, key_square)

def create_key_square(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    key_square = []

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_square.append(char)

    for i in range(65, 91):  # A-Z
        char = chr(i)
        if char == 'J':
            continue
        if char not in seen:
            key_square.append(char)

    return [key_square[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = ''.join(filter(str.isalpha, text.upper())).replace('J', 'I')
    processed = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i+1] if i + 1 < len(text) else 'X'
        if char1 == char2:
            processed += char1 + 'X'
            i += 1
        else:
            processed += char1 + char2
            i += 2
    if len(processed) % 2 != 0:
        processed += 'X'
    return processed

def find_position(letter, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

def encrypt_playfair(text, key_square):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(a, key_square)
        row2, col2 = find_position(b, key_square)

        if row1 == row2:  # Same row
            result += key_square[row1][(col1 + 1) % 5]
            result += key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            result += key_square[(row1 + 1) % 5][col1]
            result += key_square[(row2 + 1) % 5][col2]
        else:  # Rectangle
            result += key_square[row1][col2]
            result += key_square[row2][col1]
    return result

def decrypt_playfair(text, key_square):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(a, key_square)
        row2, col2 = find_position(b, key_square)

        if row1 == row2:  # Same row
            result += key_square[row1][(col1 - 1) % 5]
            result += key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            result += key_square[(row1 - 1) % 5][col1]
            result += key_square[(row2 - 1) % 5][col2]
        else:  # Rectangle
            result += key_square[row1][col2]
            result += key_square[row2][col1]
    return result

text_to_encrypt = input("Enter the plaintext: ")
key = input("Enter the key: ")
# Encrypt the plaintext
encrypted_text = playfair_cipher(text_to_encrypt, key, mode='encrypt')
print("\nEncrypted Text:", encrypted_text)
# --- User input for decryption ---
cipher_text = input("\nEnter the ciphertext to decrypt: ")
# Decrypt the ciphertext
decrypted_text = playfair_cipher(cipher_text, key, mode='decrypt')
print("Decrypted Text:", decrypted_text)
