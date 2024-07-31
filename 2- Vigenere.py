def generate_vigenere_key(plain_text, key):
    # Extend or truncate the key to match the length of the plain text
    key = list(key)
    if len(plain_text) == len(key):
        return "".join(key)
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plain_text, key):
    cipher_text = ""
    key = generate_vigenere_key(plain_text, key)
    
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            if plain_text[i].isupper():
                cipher_text += chr((ord(plain_text[i]) + ord(key[i].upper()) - 2 * 65) % 26 + 65)
            else:
                cipher_text += chr((ord(plain_text[i]) + ord(key[i].lower()) - 2 * 97) % 26 + 97)
        else:
            cipher_text += plain_text[i]

    return cipher_text

def decrypt_vigenere(cipher_text, key):
    plain_text = ""
    key = generate_vigenere_key(cipher_text, key)
    
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            if cipher_text[i].isupper():
                plain_text += chr((ord(cipher_text[i]) - ord(key[i].upper()) + 26) % 26 + 65)
            else:
                plain_text += chr((ord(cipher_text[i]) - ord(key[i].lower()) + 26) % 26 + 97)
        else:
            plain_text += cipher_text[i]

    return plain_text

# User input for Vigenère Cipher
plain_text = input("Enter plain text: ")
key = input("Enter key: ")

# Encryption
encrypted_text = encrypt_vigenere(plain_text, key)
print("Encrypted text: " + encrypted_text)

# Decryption
decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted text: " + decrypted_text)
