# Function to compute the GCD using the Euclidean algorithm (recursive version)
def gcd(a, b):
    if b == 0:
        return a
    # Recursive step: call gcd with b and the remainder of a divided by b
    else:
        return gcd(b, a % b)

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")
