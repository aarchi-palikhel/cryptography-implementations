# Diffie-Hellman Key Exchange
p = int(input("Enter prime number: "))  # A prime number
g = int(input("Enter primitive modulo of p: "))   # Primitive root modulo p

a = int(input("Enter private key of a: ")) # Private secret keys chosen by Alice (a) and Bob (b)
b= int(input("Enter private key of b: "))
# Compute public keys
A = pow(g, a, p)  # Alice's public key (A = g^a mod p)
B = pow(g, b, p)  # Bob's public key (B = g^b mod p)

# Compute the shared secret using the other party's public key
shared_secret_A = pow(B, a, p)  # Alice computes the shared secret (B^a mod p)
shared_secret_B = pow(A, b, p)  # Bob computes the shared secret (A^b mod p)

# Display the shared secret key (it should be the same for both)
print("Person A Computed Shared Secret Key:", shared_secret_A)
print("Person B Computed Shared Secret Key:", shared_secret_B)
