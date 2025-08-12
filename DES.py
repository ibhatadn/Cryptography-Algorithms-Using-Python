# Permutation tables (unchanged)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_inverse = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

EP = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

S_boxes = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 2, 8, 14, 12, 4, 7],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 1, 11, 12, 15],
        [3, 15, 13, 6, 7, 11, 4, 9, 0, 1, 10, 14, 2, 8, 12, 5],
        [6, 1, 13, 8, 7, 11, 4, 9, 0, 3, 10, 14, 12, 2, 5, 15]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 2, 3, 14, 15, 5, 12, 11],
        [5, 2, 9, 1, 14, 15, 4, 10, 0, 6, 3, 12, 11, 7, 13, 8]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 14, 13, 0, 15, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 9, 8, 3, 10, 6],
        [4, 2, 1, 11, 10, 13, 7, 6, 8, 0, 14, 9, 3, 5, 12, 15],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 3, 10, 4, 9, 5, 0, 15]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 0, 3, 14, 11, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 5, 15, 11, 14, 1, 7, 10, 8, 0, 6, 9, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 7, 10, 6, 12, 9, 5, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 6, 2, 12, 8, 15],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 8, 3, 5, 15, 13],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 3, 6, 5, 0, 11]
    ]
]

def permute(block, table):
    return ''.join(block[i - 1] for i in table)

def XOR(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(n, length=4):
    return f'{n:0{length}b}'

def f_function(right_half, subkey):
    expanded = permute(right_half, EP)
    xored = XOR(expanded, subkey)

    s_output = ''
    for i in range(8):
        row_bits = xored[i * 6] + xored[i * 6 + 5]
        col_bits = xored[i * 6 + 1:i * 6 + 5]
        row, col = binary_to_decimal(row_bits), binary_to_decimal(col_bits)
        s_output += decimal_to_binary(S_boxes[i][row][col], length=4)

    return permute(s_output, P)

def encrypt_block(block, key):
    block = permute(block, IP)
    Left_msg, Right_msg = block[:32], block[32:]

    # Perform the function
    for i in range(16):
        s_output = f_function(Right_msg, key)
        newleft = XOR(Left_msg, s_output)
        Left_msg,Right_msg=Right_msg,newleft
    return permute(Right_msg+Left_msg,IP_inverse)  # Concatenate without swap

def decrypt_block(block, key):
    block = permute(block, IP)
    
    Left_msg, Right_msg = block[:32], block[32:]

    # Use the f_function on the left half this time
    for i in range(16):
        s_output = f_function(Right_msg, key)
        newleft = XOR(Left_msg, s_output)
        Left_msg, Right_msg = Right_msg,newleft 
    return permute(Right_msg+Left_msg,IP_inverse) # Concatenate with Left_msg at the end

def binary_to_ascii(binary_str):
    binary_values = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

# Main program flow
msg = "it is cool to implement DES in python as assignment"
key = "secure"
key = ''.join(format(ord(c), '08b') for c in key)  # Convert key to binary
msg_bin = ''.join(format(ord(c), '08b') for c in msg)  # Convert message to binary
print('Actual message:', msg_bin)
print("round_key----->",key)
msg_bin=[msg_bin[i:i+64] for i in range(0,len(msg_bin),64)]

# Encrypt the message
em = ''
for i in range(len(msg_bin)):
    # Pad the plaintext block to ensure it's 64 bits long
    plaintext = msg_bin[i] + '0' * (64 - len(msg_bin[i])) if len(msg_bin[i]) < 64 else msg_bin[i]
    em += encrypt_block(plaintext, key)

# Break the encrypted message back into 64-bit blocks
encrypted_blocks = [em[i:i + 64] for i in range(0, len(em), 64)]
print("\n\nEncrypted binary:", em)
print("Encrypted ASCII:", binary_to_ascii(em),"\n\n")
print()
print()
# Decrypt the message
decrypted_msg = ''
for block in encrypted_blocks:
    decrypted_msg += decrypt_block(block, key)

print("Decrypted binary:", decrypted_msg)
print("Decrypted ASCII:", binary_to_ascii(decrypted_msg))

