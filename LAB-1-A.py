def encrypt_caesar(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

def decrypt_caesar(ciphertext, s):
    result = ""
    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

# User input for Additive (Caesar) Cipher
text = input("Enter text: ")
s = int(input("Enter shift (s): "))

encrypted_text = encrypt_caesar(text, s)
print("Encrypted text: " + encrypted_text)

decrypted_text = decrypt_caesar(encrypted_text, s)
print("Decrypted text: " + decrypted_text)
