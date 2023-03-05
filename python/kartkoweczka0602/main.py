##grupa 2

a=int(input("wybierz zadanie (1-3) "))

if(a==1):
    liczby = [3, 2, 4, 14, 23, 35, 22, 6, 8]
    liczby.sort()
    print("Najmniejsza liczba to: ", liczby[0])
elif(a==2):
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
elif(a==3):
    def main():
        N = [5, 3, 2, 1]
        R = int(input("Podaj reszte do wyplacenia: "))
        i = 0
        while R > 0:
            if R >= N[i]:
                P = R // N[i]
                R = R - (N[i] * P)
                print(f"{N[i]} x {P}")
            i += 1

    if __name__ == "__main__":
        main()
