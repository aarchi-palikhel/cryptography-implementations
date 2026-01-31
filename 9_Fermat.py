import random

def fermat_primality_test(n, k=5):
    # Step 1: Check base cases
    if n < 2:
        return "Composite"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0:
        return "Composite"
    
    for _ in range(k):
        a = random.randint(2, n - 2)  
        if pow(a, n - 1, n) != 1: 
            return "Composite" 

    return "Probably Prime"

n = int(input("Enter the number to test for primality: "))
k = int(input("Enter the number of iterations (k) for the test (default is 5): ") or 5)

result = fermat_primality_test(n, k)
print(f"Result for {n}: {result}")