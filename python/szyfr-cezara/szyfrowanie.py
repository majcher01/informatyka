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

plaintext = input('Wprowadz tekst: ')
shift = int(input('Wprowadz przesuniecie: '))
ciphertext = encrypt(plaintext, shift)
print(f'Zaszyfrowany tekst: {ciphertext}')