print("Zadania:\n1.Ciag liczb 0-4\n2.ciag zdefiniowany przez uzytkownika\n3.Ciag od 6 do 30 co 5")
zadanie = int(input("\nWprowadz numer zadania: "))

if(zadanie == 1):
    for x in range(0, 5):
        print(str(x))

elif(zadanie == 2):

    def ciag(start, stop, skok):
        for i in range(start, stop, skok):
            print(str(i))

    start=int(input("wprowadz pierwsza liczbe: "))
    stop=int(input("wprowadz ostatnia liczbe: "))
    skok=int(input("wprowadz skok petli: "))
    stop=stop+1
    ciag(start, stop, skok)
elif(zadanie == 3):
    for i in range(6, 31, 6):
        print(str(i))

elif(zadanie == 4):
    for i in range(0, 10, 1):
        if(i == 2 or i==4 or i==5 or i==7 or i==8):
            continue
        print(str(i))
elif(zadanie == 5):
    for i in range(53, 57, 1):
        print(str(i))
elif(zadanie == 6):
    bok = int(input("podaj bok kwadratu: "))
    for i in range(bok):
        for i in range(bok):
            print("#", end = ' ')
        print()

elif(zadanie == 7):
    a = int(input("Podaj pierwszy bok: "))
    b = int(input("Podaj drugi bok: "))

    for i in range(1, a+1):
        for j in range(1, b+1):
            if(i==1 or i==a or j==1 or j==b):
                print(end="#  ")
            else:
                print(end="   ")
        print(end="\n\n")






