# Python3 implementation of
# Columnar Transposition
import math             # This line imports the math module, which provides mathematical functions like ceil that we'll use for calculations.

key = "HACK"            # This sets the key for the cipher. The key determines the order of columns in the matrix.

# Encryption




def encryptMessage(msg):            # This defines a function named encryptMessage that takes a message as input.
    cipher = ""                     # cipher: This variable will store the encrypted message.

    # track key indices
    k_indx = 0                          # k_indx: This index keeps track of the current key character.
    msg_len = float(len(msg))           # msg_len: The length of the message.
    msg_lst = list(msg)                 # msg_lst: The message converted into a list of characters.
    key_lst = sorted(list(key))         # key_lst: The key sorted alphabetically.

    # calculate column of the matrix
    col = len(key)                                  # col: The number of columns in the matrix (equal to the key length).

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))             # row: The number of rows in the matrix, calculated based on the message length and column count.

    # add the padding character '_' in empty
    # the empty cell of the matix
    fill_null = int((row * col) - msg_len)            # fill_null: The number of padding characters needed to fill the matrix.
    msg_lst.extend('_' * fill_null)                   # msg_lst.extend('_' * fill_null): This adds padding characters ('_') to the message list to fill the matrix.

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i: i + col]                      # This line creates a matrix by dividing the message list into rows of length col.
              for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key                   # This loop iterates over each column of the matrix.
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])             # curr_idx: The index of the current column in the original key order.
        cipher += ''.join([row[curr_idx]                  # The characters from the current column are added to the cipher string.
                           for row in matrix])
        k_indx += 1                                        # k_indx is incremented to move to the next key character.

    return cipher                                          # The function returns the encrypted message.

# Decryption


def decryptMessage(cipher,key):                          # This defines a function named decryptMessage that takes the cipher text and the key as input.
    msg = ""                                              # Similar to the encryption part, variables are initialized to store the decrypted message, indices, and matrix.

    # track key indices
    k_indx = 0

    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))    # Type Casting the length of cipher
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):                                       #  This loop fills the decryption matrix column-wise based on the sorted key.
        curr_idx = key.index(key_lst[k_indx])                   # The characters from the cipher text are placed into the corresponding positions in the matrix.

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # convert decrypted msg matrix into a string
    try:                                                     # The matrix is flattened and converted back into a string.
        msg = ''.join(sum(dec_cipher, []))                   # A try-except block is used to handle potential errors, such as repeating words in the cipher text.
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')                            # Any padding characters ('_') are removed from the decrypted message.

    if null_count  > 0:
        return msg[: -null_count]

    return msg


# Driver Code                                             # This part takes user input for the message to be encrypted or decrypted.
msg = input("Enter a message you want to encrypt:")        # It calls the encryptMessage and decryptMessage functions to perform the respective operations.

cipher = encryptMessage(msg)
print(f"Encrypted Message: {cipher}")
print("press enter to continue...")

msg = input("Enter the encrypted message you want to decrypt:")
decrypted_msg =decryptMessage(msg,key)
print("Decryped Message: {}".
    format(decrypted_msg))
      # format(decryptMessage(cipher)))                        # The results are printed to the console.
