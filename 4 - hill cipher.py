import numpy as np

def prepare_text(text):
    text = text.upper().replace(' ', '')  # Remove spaces and convert to uppercase
    text = [ord(char) - ord('A') for char in text]  # Convert to numerical values
    if len(text) % 2 != 0:
        text.append(ord('X') - ord('A'))
    return text

def matrix_multiply(A, B):
    return np.dot(A, B) % 26

def hill_cipher_encrypt(plain_text, key_matrix):
    text_numbers = prepare_text(plain_text)

    text_matrix = np.array(text_numbers).reshape(-1, 2).T

    cipher_matrix = matrix_multiply(key_matrix, text_matrix)

    cipher_text = ''.join(chr(num + ord('A')) for num in cipher_matrix.flatten())
    return cipher_text


def get_key_matrix():
    print("Enter the key matrix as a single line of space-separated values:")
    values = list(map(int, input().split()))
    size = int(len(values) ** 0.5)
    key_matrix = np.array(values).reshape(size, size)
    return key_matrix

plain_text = input("Enter plaintext: ")

key_matrix = get_key_matrix()

encrypted_text = hill_cipher_encrypt(plain_text, key_matrix)
print("Encrypted text:", encrypted_text)
