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
    choice = input("Chcesz zaszyfrowac tekst (1) czy odszyfrowac (2) ? ").upper()
    if choice == '1':
        plaintext = input("Wprowadz tekst: ")
        shift = int(input("Wprowadz przesuniecie: "))
        ciphertext = encrypt(plaintext, shift)
        print("Zaszyfrowany tekst: " + ciphertext)
    elif choice == '2':
        ciphertext = input("Wprowadz tekst: ")
        shift = int(input("Wprowadz przesuniecie: "))
        plaintext = decrypt(ciphertext, shift)
        print("Odszyfrowany tekst: " + plaintext)
    repeat = input("Czy chcesz powtorzyc ? (T/N) ").upper()
    if repeat != 'T':
        break