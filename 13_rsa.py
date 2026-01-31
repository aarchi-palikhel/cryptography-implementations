def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = gcd_extended(e, phi)
    if gcd != 1:
        return None  # No modular inverse
    else:
        return x % phi

# Step 1: Choose primes
p = int(input("Enter 1st prime num: "))
q = int(input("Enter 2nd prime num: "))
# Step 2: Compute n
n = p * q
print("n =", n)
# Step 3: Compute totient phi(n)
phi = (p - 1) * (q - 1)
print("phi =", phi)
# Step 4: Choose public exponent e
e = 7  # manually chosen, must be coprime with phi
print("e =", e)
# Step 5: Compute private key exponent d
d = mod_inverse(e, phi)
print("d =", d)
# Step 6: Public and Private Keys
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')
# Encryption
msg = int(input("Plaintext message: "))  # plaintext message
print("Original Message:", msg)
cipher = pow(msg, e, n)
print("Encrypted Message:", cipher)
# Decryption
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)
