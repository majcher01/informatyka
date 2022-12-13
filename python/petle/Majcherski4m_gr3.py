zadanie = int(input("Wybierz zadanie (1-3): "))

if(zadanie==1):
    for i in range(2, 15, 3):
        print(str(i), end=",")
    print("\n")
elif(zadanie==2):
    liczba = int(input("podaj koncowa liczbe "))
    suma=0
    for i in range(1, liczba+1):
        suma=suma+i
    wynik=suma/liczba
    print(str(wynik))
elif(zadanie==3):
    koniec=int(input("Podaj liczbe: "))
    i=1
    while(i<koniec):
        print(str(i**2))
        i=i+1
else:
    print("Niepoprawny numer zadania")