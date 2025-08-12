from os import urandom
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def cbc_xor_block(block, previous_block):
    """
    XORs a plaintext block with the previous ciphertext block (or IV).
    
    Args:
        block (bytes): The current plaintext block.
        previous_block (bytes): The previous ciphertext block (or IV for the first block).
        
    Returns:
        bytes: The XOR result, ready for encryption.
    """
    return xor_bytes(block, previous_block)

def cbc_encrypt(key, plaintext):
    block_size = 8  # DES block size is 8 bytes
    iv = urandom(block_size)  # Generate a random IV
    cipher = DES.new(key, DES.MODE_CBC, iv)  # Initialize DES in CBC mode with IV

    # Pad the plaintext to be a multiple of block size
    padded_plaintext = pad(plaintext, block_size)
    
    # Encrypt each block using CBC XOR operation
    ciphertext = b''
    previous_block = iv

    for i in range(0, len(padded_plaintext), block_size):
        block = padded_plaintext[i:i + block_size]
        xor_result = cbc_xor_block(block, previous_block)  # XOR with previous block (or IV for the first block)
        encrypted_block = cipher.encrypt(xor_result)  # Encrypt the XOR result
        ciphertext += encrypted_block
        previous_block = encrypted_block  # Update previous block for next iteration

    return iv + ciphertext  # Prepend IV for use in decryption

def cbc_decrypt(key, ciphertext):
    block_size = 8  # DES block size is 8 bytes
    iv = ciphertext[:block_size]  # Extract the IV from the beginning of the ciphertext
    cipher = DES.new(key, DES.MODE_CBC, iv)  # Initialize DES in CBC mode with IV

    decrypted_text = b''
    previous_block = iv

    for i in range(block_size, len(ciphertext), block_size):
        encrypted_block = ciphertext[i:i + block_size]
        decrypted_block = cipher.decrypt(encrypted_block)  # Decrypt the block
        xor_result = cbc_xor_block(decrypted_block, previous_block)  # XOR with previous block (or IV for the first block)
        decrypted_text += xor_result
        previous_block = encrypted_block  # Update previous block for next iteration

    # Unpad the decrypted text and return
    return unpad(decrypted_text, block_size)

# Example usage
if __name__ == "__main__":
    key = urandom(8)  # DES key must be exactly 8 bytes
    plaintext = b'HEY This is a secret message.'

    ciphertext = cbc_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_plaintext = cbc_decrypt(key, ciphertext)
    print("Decrypted:", decrypted_plaintext)