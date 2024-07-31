def multiplicative_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def encrypt_affine(text, a, b):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - 65) * a + b) % 26 + 65)
        elif char.islower():
            result += chr(((ord(char) - 97) * a + b) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

def decrypt_affine(ciphertext, a, b):
    a_inv = multiplicative_inverse(a, 26)
    result = ""
    for char in ciphertext:
        if char.isupper():
            result += chr((a_inv * ((ord(char) - 65 - b) % 26 + 26) % 26) + 65)
        elif char.islower():
            result += chr((a_inv * ((ord(char) - 97 - b) % 26 + 26) % 26) + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

# User input for Affine Cipher
text = input("Enter text: ")
a = int(input("Enter multiplicative key (a): "))
b = int(input("Enter additive key (b): "))

encrypted_text = encrypt_affine(text, a, b)
print("Encrypted text: " + encrypted_text)

decrypted_text = decrypt_affine(encrypted_text, a, b)
print("Decrypted text: " + decrypted_text)
