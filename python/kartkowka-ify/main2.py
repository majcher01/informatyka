bok1=int(input("podaj bok a "))
bok2=int(input('podaj bok b '))
kat=int(input('podaj kat miedzy bokami '))

if(kat==90 and bok1!=0 and bok2!=0):
    bokc=(bok1**2)+(bok2**2)
    wynik=bokc**(1/2)
    print('dlugosc przeciwprostokatnej to '+str(wynik))
else:
    print('nie mozna obliczyc dlugosci przeciwprostokatnej')
