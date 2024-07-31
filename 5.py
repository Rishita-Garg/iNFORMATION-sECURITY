def decrypt_caesar(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        elif char == ' ':
            result += char
        else:
            result += char
    return result

text = input("Enter text: ")
s = int(input("Enter shift (s): "))

decrypted_text = decrypt_caesar(text, s)
print("Decrypted text:", decrypted_text)

'''
the plaintext found by John is BZMIACAM and also the
attack corresponds to known-plaintext attack as
John understood the key because he knew previously used 
cipher-text and its respective plaintext.
'''