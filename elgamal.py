import random
from hashlib import sha256

# Helper function: Modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod
    return result

# Generate keys
def generate_keys():
    # Large prime number (p) and generator (g)
    p = 467  # Example small prime, replace with a large prime in real applications
    g = 2    # Generator
    private_key = random.randint(1, p - 2)  # Private key: a random integer 1 < x < p-1
    public_key = mod_exp(g, private_key, p)  # Public key: g^x mod p
    return p, g, private_key, public_key

# Create signature
def sign_message(message, p, g, private_key):
    k = random.randint(1, p - 2)
    while gcd(k, p - 1) != 1:  # Ensure k is coprime to p-1
        k = random.randint(1, p - 2)
    r = mod_exp(g, k, p)
    hash_value = int(sha256(message.encode()).hexdigest(), 16)
    s = (pow(k, -1, p - 1) * (hash_value - private_key * r)) % (p - 1)
    return r, s

# Verify signature
def verify_signature(message, r, s, p, g, public_key):
    if not (0 < r < p):
        return False
    hash_value = int(sha256(message.encode()).hexdigest(), 16)
    v1 = mod_exp(public_key, r, p) * mod_exp(r, s, p) % p
    v2 = mod_exp(g, hash_value, p)
    return v1 == v2

# Greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    print("Generating keys...")
    p, g, private_key, public_key = generate_keys()
    print(f"Public Key: (p={p}, g={g}, y={public_key})")
    print(f"Private Key: x={private_key}")

    message = "This is a test message."
    print(f"\nSigning message: '{message}'")
    r, s = sign_message(message, p, g, private_key)
    print(f"Signature: (r={r}, s={s})")

    print("\nVerifying signature...")
    is_valid = verify_signature(message, r, s, p, g, public_key)
    print(f"Signature valid: {is_valid}")
