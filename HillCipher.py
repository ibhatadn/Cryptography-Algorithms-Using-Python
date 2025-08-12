"""
Please note: if you are planning to run this code using the simple python interpreter,
use pip install egcd or py -m pip install egcd 
"""
# For Installing egcd on google-colab use:
!pip install egcd

"""
Necessary Modules:
"""
import numpy as np
from egcd import egcd

"""
Pre-requisites:
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet),"\n")
letter_to_index = dict(zip(alphabet, range(len(alphabet)))) # maps letters to numbers
print(letter_to_index, "\n")
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) # maps numbers to letters
print(index_to_letter, "\n")

def matrix_mod_inv(matrix, modulus):
    """
    We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant inverse value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverse of matrix in mod 26
    """

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)            # 9
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)            # (1, 3, -1)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)
    return matrix_modulus_inv
 
def encrypt(message, K):
    """
    C = E(K,P) = K*P (mod X) -- X is length of alphabet used
    """
    encrypted = ""
    message_in_numbers = []

    for letter in message:                                             #  [c  a   u   g   h   t]
        message_in_numbers.append(letter_to_index[letter])             #  [2  0   20  6   7   19]

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]                   # creates subsets of message_in_numbers list according to the order of key matrix (which is 2 in this case)
        for i in range(0, len(message_in_numbers), int(K.shape[0]))   # [[2, 6], [20, 6], [7, 19]]
        ]
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]        # P = Vector of plaintext (that has been mapped to numbers)
        while P.shape[0] != K.shape[0]:
          P = np.append(P, letter_to_index["x"])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)        # Matrix multiplication
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted
    
def decrypt(cipher, Kinv):
    """
    P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used
    """

    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]        # C = Vector of Ciphered text (in numbers)
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted
def main():
    # message = 'paymoremoney'
    message = "caught"


    # K = Matrix which is our 'Secret Key'
    K = np.matrix([[3, 3], [2, 5]])


    # K = np.matrix([[6, 24, 1], [13,16,10], [20,17,15]]) # for length of alphabet = 26
    # K = np.matrix([[3,10,20],[20,19,17], [23,78,17]]) # for length of alphabet = 27
    Kinv = matrix_mod_inv(K, len(alphabet))
    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)
    
    
main()