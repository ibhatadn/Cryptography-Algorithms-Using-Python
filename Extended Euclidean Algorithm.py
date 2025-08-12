def extended_euclidean(a, b):
    """
    Compute the GCD of a and b, and find integers x and y such that:
    a * x + b * y = GCD(a, b)
    """
    if a == 0:
        return b, 0, 1  # Base case: GCD is b, x = 0, y = 1
    else:
        gcd, x1, y1 = extended_euclidean(b % a, a)  # Recursive call
        x = y1 - (b // a) * x1  # Update x
        y = x1  # Update y
        return gcd, x, y

# Example usage
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

gcd, x, y = extended_euclidean(n1, n2)
print(f"GCD of {n1} and {n2} is: {gcd}")
print(f"Coefficients x and y are: {x}, {y}") 
