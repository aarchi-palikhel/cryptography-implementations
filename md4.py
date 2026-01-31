import struct

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md4(message):
    # Initial values
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    # Message preprocessing
    message = bytearray(message, 'utf-8') if isinstance(message, str) else bytearray(message)
    orig_len = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += struct.pack('<Q', orig_len)

    # Define auxiliary functions
    def F(x, y, z): return (x & y) | (~x & z)
    def G(x, y, z): return (x & y) | (x & z) | (y & z)
    def H(x, y, z): return x ^ y ^ z

    def round1(a, b, c, d, k, s): return left_rotate((a + F(b, c, d) + X[k]) & 0xFFFFFFFF, s)
    def round2(a, b, c, d, k, s): return left_rotate((a + G(b, c, d) + X[k] + 0x5A827999) & 0xFFFFFFFF, s)
    def round3(a, b, c, d, k, s): return left_rotate((a + H(b, c, d) + X[k] + 0x6ED9EBA1) & 0xFFFFFFFF, s)

    # Process each 512-bit block
    for offset in range(0, len(message), 64):
        X = list(struct.unpack('<16I', message[offset:offset+64]))
        a, b, c, d = A, B, C, D

        # Round 1
        s = [3, 7, 11, 19]
        for i in range(0, 16, 4):
            a = round1(a, b, c, d, i, s[0])
            d = round1(d, a, b, c, i+1, s[1])
            c = round1(c, d, a, b, i+2, s[2])
            b = round1(b, c, d, a, i+3, s[3])

        # Round 2
        s = [3, 5, 9, 13]
        idxs = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
        for i in range(0, 16, 4):
            a = round2(a, b, c, d, idxs[i], s[0])
            d = round2(d, a, b, c, idxs[i+1], s[1])
            c = round2(c, d, a, b, idxs[i+2], s[2])
            b = round2(b, c, d, a, idxs[i+3], s[3])

        # Round 3
        s = [3, 9, 11, 15]
        idxs = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        for i in range(0, 16, 4):
            a = round3(a, b, c, d, idxs[i], s[0])
            d = round3(d, a, b, c, idxs[i+1], s[1])
            c = round3(c, d, a, b, idxs[i+2], s[2])
            b = round3(b, c, d, a, idxs[i+3], s[3])

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    return struct.pack('<4I', A, B, C, D).hex()

# Example usage
if __name__ == "__main__":
    text = input("Enter the message: ")
    print("MD4 Hash:", md4(text))
