import struct

def sha1(message):
    # 1. Padding the message
    original_length = len(message) * 8  # Length in bits
    message = bytearray(message, 'utf-8')  # Convert to bytearray
    message.append(0x80)  # Append the bit '1' to the message
    
    while (len(message) * 8) % 512 != 448:  # Pad with '0' bits until length % 512 = 448
        message.append(0x00)
    
    # Append the original length as a 64-bit big-endian integer
    message += struct.pack(">Q", original_length)

    # 2. Initialize variables (SHA-1 constants)
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # 3. Process the message in 512-bit chunks
    for i in range(0, len(message), 64):  # Each chunk is 64 bytes = 512 bits
        chunk = message[i:i + 64]
        
        # Break chunk into 16 big-endian 32-bit words
        w = list(struct.unpack(">16I", chunk)) + [0] * 64

        # Extend the 16 words into 80 words
        for j in range(16, 80):
            w[j] = (w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16]) & 0xFFFFFFFF
            w[j] = (w[j] << 1 | w[j] >> 31) & 0xFFFFFFFF  # Left rotate

        # Initialize hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop (80 rounds)
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (a << 5 | a >> 27) + f + e + k + w[j] & 0xFFFFFFFF
            e = d
            d = c
            c = (b << 30 | b >> 2) & 0xFFFFFFFF
            b = a
            a = temp

        # Add this chunk's hash to result so far
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash value as a 160-bit number
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

# Test the function
message = "Hello, World!"
hash_value = sha1(message)
print("SHA-1 Hash:", hash_value)
