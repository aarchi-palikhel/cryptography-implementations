def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            P = ord(char) - base
            C = (P + key) % 26
            result += chr(C + base)
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            C = ord(char) - base
            P = (C + 26 - key) % 26
            result += chr(P + base)
        else:
            result += char
    return result
text = input("Enter the plaintext: ")
key = int(input("Enter the key (shift value): "))
encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)
print("\nEncrypted text:", encrypted)
print("Decrypted text:", decrypted)
