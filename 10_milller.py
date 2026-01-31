import random

def miller_rabin(n, k=5):
    if n < 2:
        return "Composite"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0:
        return "Composite"
    
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2) 
        x = pow(a, d, n)  

        if x == 1 or x == n - 1:
            continue  

        for _ in range(s - 1):
            x = pow(x, 2, n) 
            if x == 1:
                return "Composite"  
            if x == n - 1:
                break 
        else:
            return "Composite" 
    return "Probably Prime"

n = int(input("Enter a number to check for primality: "))
k = int(input("Enter the number of iterations: "))
result = miller_rabin(n, k)
print(f"Result for {n}: {result}")