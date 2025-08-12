import random
from sympy import gcd, mod_inverse, isprime

# Function to generate a random prime number of given bit length
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num
# Step 1: Key Generation
def generate_keys(bit_length):
    # Generate two large prime numbers p and q
    p = generate_prime(int(bit_length / 2))
    q = generate_prime(int(bit_length / 2))
    
    # Calculate n = p * q
    n = p * q
    
   # Calculate φ(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)
    
    # Select e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
    
    # Calculate d such that e * d ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi)
    
    # Public key: (e, n), Private key: (d, n)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Step 2: Encryption (encrypt the entire message as a single block)
def encrypt(plain_text, public_key):
    e, n = public_key
    
    # Convert the entire message to an integer
    message_as_int = int.from_bytes(plain_text.encode(), 'big')

    # Encrypt the message: C = M^e mod n
    cipher_text = pow(message_as_int, e, n)
    return cipher_text

# Step 3: Decryption (decrypt the single block back to the message)
def decrypt(cipher_text, private_key):
    d, n = private_key
    # Decrypt the cipher: M = C^d mod n
    message_as_int = pow(cipher_text, d, n)
    # Convert the integer back to the original message
    plain_text = message_as_int.to_bytes((message_as_int.bit_length() + 7) // 8, 'big').decode()
    return plain_text


def main():
    # Key generation (using 1024-bit numbers)
    public_key, private_key = generate_keys(1024)
    
    # print("Public Key:", public_key)
    # print("Private Key:", private_key)
    
    # Encrypt a message
    message = input("Enter the message: ")
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
    
