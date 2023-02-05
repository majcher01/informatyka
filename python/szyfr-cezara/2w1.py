# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def encrypt_caesar(plaintext, shift):
#     ciphertext = ""
#     for char in plaintext:
#         if char.upper() in letters:
#             char_index = letters.index(char.upper())
#             shift_char = letters[(char_index + shift) % 26]
#             if char.islower():
#                 ciphertext += shift_char.lower()
#             else:
#                 ciphertext += shift_char
#         else:
#             ciphertext += char
#     return ciphertext

# def decrypt_caesar(ciphertext, shift):
#     plaintext = ""
#     for char in ciphertext:
#         if char.upper() in letters:
#             char_index = letters.index(char.upper())
#             shift_char = letters[(char_index - shift + 26) % 26]
#             if char.islower():
#                 plaintext += shift_char.lower()
#             else:
#                 plaintext += shift_char
#         else:
#             plaintext += char
#     return plaintext

# def main():
#     action = input("Enter 'e' to encrypt or 'd' to decrypt: ")
#     if action == 'e':
#         plaintext = input("Enter the text to be encrypted: ")
#         shift = int(input("Enter the shift value: "))
#         ciphertext = encrypt_caesar(plaintext, shift)
#         print(f"Encrypted text: {ciphertext}")
#     elif action == 'd':
#         ciphertext = input("Enter the text to be decrypted: ")
#         shift = int(input("Enter the shift value: "))
#         plaintext = decrypt_caesar(ciphertext, shift)
#         print(f"Decrypted text: {plaintext}")
#     else:
#         print("Invalid action")

# if __name__ == "__main__":
#     main()

#Z PETLA

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.upper() in LETTERS:
            index = (LETTERS.index(char.upper()) + shift) % 26
            if char.isupper():
                ciphertext += LETTERS[index]
            else:
                ciphertext += LETTERS[index].lower()
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.upper() in LETTERS:
            index = (LETTERS.index(char.upper()) - shift) % 26
            if char.isupper():
                plaintext += LETTERS[index]
            else:
                plaintext += LETTERS[index].lower()
        else:
            plaintext += char
    return plaintext

while True:
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    if choice == 'E':
        plaintext = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        ciphertext = encrypt(plaintext, shift)
        print("Encrypted message: " + ciphertext)
    elif choice == 'D':
        ciphertext = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift value: "))
        plaintext = decrypt(ciphertext, shift)
        print("Decrypted message: " + plaintext)
    repeat = input("Would you like to repeat the process? (Y/N) ").upper()
    if repeat != 'Y':
        break