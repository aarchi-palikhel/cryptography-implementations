from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Padding for block size (AES = 16 bytes block)
def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# AES Encryption
def aes_encrypt(plaintext, key):
    key = key[:16].ljust(16, b'\0')  # Ensure 16-byte key
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    return base64.b64encode(iv + ciphertext).decode()

# AES Decryption
def aes_decrypt(ciphertext_b64, key):
    key = key[:16].ljust(16, b'\0')  # Ensure 16-byte key
    raw = base64.b64decode(ciphertext_b64)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    key = b'mysecretpassword'  # Must be 16, 24, or 32 bytes
    message = input("Enter message to encrypt: ").encode()

    encrypted = aes_encrypt(message, key)
    print("Encrypted (base64):", encrypted)

    decrypted = aes_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
