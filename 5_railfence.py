def rail_fence_encrypt(text, rails):
    matrix = [["" for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, 1
    # Fill the matrix in a zigzag pattern
    for i, char in enumerate(text):
        matrix[row][i] = char
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1
    # Join the rows to get the encrypted text
    encrypted_text = "".join(["".join(row) for row in matrix])
    return encrypted_text.replace(" ", "")

def rail_fence_decrypt(text, rails):
    # Create the empty matrix
    matrix = [["" for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, 1
    # Mark positions in the matrix where the characters will be placed
    for i in range(len(text)):
        matrix[row][i] = "*"
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1
    # Place the encrypted text characters into the marked positions
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if matrix[i][j] == "*":
                matrix[i][j] = text[index]
                index += 1
    # Read the matrix row by row to construct the decrypted text
    decrypted_text = ""
    row, direction = 0, 1
    for i in range(len(text)):
        decrypted_text += matrix[row][i]
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1
    return decrypted_text

p_t = input("Enter the text to encrypt: ")
rails = int(input("Enter the number of rails: "))
print("Rail Fence Encrypted Text:", rail_fence_encrypt(p_t, rails))
c_t = input("Enter the text to decrypt: ")
print("Rail Fence Decrypted Text:", rail_fence_decrypt(c_t, rails))
