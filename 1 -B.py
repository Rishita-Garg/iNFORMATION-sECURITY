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

def encrypt_multiplicative(text, a):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - 65) * a) % 26 + 65)
        elif char.islower():
            result += chr(((ord(char) - 97) * a) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

def decrypt_multiplicative(ciphertext, a):
    a_inv = multiplicative_inverse(a, 26)
    result = ""
    for char in ciphertext:
        if char.isupper():
            result += chr(((ord(char) - 65) * a_inv) % 26 + 65)
        elif char.islower():
            result += chr(((ord(char) - 97) * a_inv) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

# User input for Multiplicative Cipher
text = input("Enter text: ")
a = int(input("Enter multiplicative key (a): "))

encrypted_text = encrypt_multiplicative(text, a)
print("Encrypted text: " + encrypted_text)

decrypted_text = decrypt_multiplicative(encrypted_text, a)
print("Decrypted text: " + decrypted_text)
