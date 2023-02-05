LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext.upper():
        if char in LETTERS:
            index = (LETTERS.index(char) + shift) % 26
            ciphertext += LETTERS[index]
        else:
            ciphertext += char
    return ciphertext

plaintext = input('Enter the plaintext: ')
shift = int(input('Enter the shift value: '))
ciphertext = encrypt(plaintext, shift)
print(f'The encrypted message is: {ciphertext}')