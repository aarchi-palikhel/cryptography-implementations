def modular_addition(a, b, mod):
    return (a + b) % mod

def modular_subtraction(a, b, mod):
    return (a - b) % mod

def modular_multiplication(a, b, mod):
    return (a * b) % mod

# Function to perform modular exponentiation
def modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod  # In case base is larger than mod
    while exponent > 0:
        if exponent % 2 == 1:  # If the exponent is odd
            result = (result * base) % mod
        exponent = exponent // 2  # Divide the exponent by 2
        base = (base * base) % mod  # Square the base
    return result

# Example usage
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
mod = int(input("Enter the mod: "))

# Performing Modular Arithmetic Operations
add_result = modular_addition(a, b, mod)
sub_result = modular_subtraction(a, b, mod)
mul_result = modular_multiplication(a, b, mod)
exp_result = modular_exponentiation(a, b, mod)

print(f"Modular Addition: ({a} + {b}) % {mod} = {add_result}")
print(f"Modular Subtraction: ({a} - {b}) % {mod} = {sub_result}")
print(f"Modular Multiplication: ({a} * {b}) % {mod} = {mul_result}")
print(f"Modular Exponentiation: {a}^{b} % {mod} = {exp_result}")
