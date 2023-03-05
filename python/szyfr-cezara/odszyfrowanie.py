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

ciphertext = input('Wprowadz teskt: ')
shift = int(input('Wprowadz przesuniecie: '))
plaintext = decrypt(ciphertext, shift)
print(f'Odszyfrowany teskt to: {plaintext}')