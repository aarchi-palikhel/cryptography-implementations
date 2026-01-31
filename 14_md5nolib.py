import struct
import math

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    # Initialize variables
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Constants
    s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
    ]

    # Use precomputed K values instead of calculating them each time
    K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    # Convert message to bytes
    message = bytearray(message, 'utf-8') if isinstance(message, str) else bytearray(message)
    orig_len = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF

    # Pre-processing: add padding
    message.append(0x80)
    while (len(message) % 64) != 56:
        message.append(0)

    # Append original length in bits
    message += struct.pack('<Q', orig_len)

    # Process each 512-bit block
    for offset in range(0, len(message), 64):
        a, b, c, d = A, B, C, D
        chunk = message[offset:offset+64]
        M = struct.unpack('<16I', chunk)

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | ((~b) & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:  # 48 <= i <= 63
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Output in little-endian
    return struct.pack('<4I', A, B, C, D).hex()

# Example usage
if __name__ == "__main__":
    text = input("Enter the message: ")
    print("MD5 Hash:", md5(text))