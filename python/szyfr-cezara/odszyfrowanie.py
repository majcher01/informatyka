LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext.upper():
        if char in LETTERS:
            index = (LETTERS.index(char) - shift) % 26
            plaintext += LETTERS[index]
        else:
            plaintext += char
    return plaintext

ciphertext = input('Enter the ciphertext: ')
shift = int(input('Enter the shift value: '))
plaintext = decrypt(ciphertext, shift)
print(f'The decrypted message is: {plaintext}')