def mod_inv(a, mod):
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None

def matrix_mod_inverse_2x2(matrix, mod):
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % mod
    det_inv = mod_inv(det, mod)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod {}".format(mod))
    
    adjugate = [[d, -b], [-c, a]]
    inverse = [[(det_inv * adjugate[i][j]) % mod for j in range(2)] for i in range(2)]
    return inverse

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding with X
    nums = [ord(c) - ord('A') for c in plaintext]
    ciphertext = ''
    for i in range(0, len(nums), 2):
        x = nums[i]
        y = nums[i + 1]
        c1 = (key[0][0] * x + key[0][1] * y) % 26
        c2 = (key[1][0] * x + key[1][1] * y) % 26
        ciphertext += chr(c1 + ord('A')) + chr(c2 + ord('A'))
    return ciphertext

def decrypt(ciphertext, key):
    key_inv = matrix_mod_inverse_2x2(key, 26)
    nums = [ord(c) - ord('A') for c in ciphertext]
    plaintext = ''
    for i in range(0, len(nums), 2):
        x = nums[i]
        y = nums[i + 1]
        p1 = (key_inv[0][0] * x + key_inv[0][1] * y) % 26
        p2 = (key_inv[1][0] * x + key_inv[1][1] * y) % 26
        plaintext += chr(p1 + ord('A')) + chr(p2 + ord('A'))
    return plaintext

key = [[3, 3], [2, 5]]
plaintext = input("Enter the plaintext: ").replace(" ", "").upper()  # Remove spaces and convert to uppercase
print("Plaintext:", plaintext)
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
