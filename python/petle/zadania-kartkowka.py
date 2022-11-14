print("Zadania:\n1.Ciag liczb 0-4\n2.ciag zdefiniowany przez uzytkownika\n3.Ciag od 6 do 30 co 5")
zadanie = int(input("\nWprowadz numer zadania: "))

#wyswietlenie liczb od 1 do 4

if(zadanie == 1):
    for x in range(0, 5):
        print(str(x))

#petla robiona funkcja w ktorej user podaje parametry

elif(zadanie == 2):

    def ciag(start, stop, skok):
        for i in range(start, stop, skok):
            print(str(i))

    start=int(input("wprowadz pierwsza liczbe: "))
    stop=int(input("wprowadz ostatnia liczbe: "))
    skok=int(input("wprowadz skok petli: "))
    stop=stop+1
    ciag(start, stop, skok)

#petla od 6 do 30 co 6

elif(zadanie == 3):
    for i in range(6, 31, 6):
        print(str(i))


#petla od 0 do 9 z pominieciem niektorych elementow

elif(zadanie == 4):
    for i in range(0, 10, 1):
        if(i == 2 or i==4 or i==5 or i==7 or i==8):
            continue
        print(str(i))

#petla od 53 do 56

elif(zadanie == 5):
    for i in range(53, 57, 1):
        print(str(i))

#zamalowany kwadrat, user podaje dlugosc

elif(zadanie == 6):
    bok = int(input("podaj bok kwadratu: "))
    for i in range(bok):
        for i in range(bok):
            print("#", end = ' ')
        print()


#pusty prostokat/kwadrat, user podaje oba boki

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
        

#zamalowany trojkat, user podaje bok

elif(zadanie == 8):
    a = int(input("Podaj bok "))


    for i in range(a):
        for j in range(i + 1):
            print("*", end=" ")
        print("")

#pusty kwadrat, user podaje jeden bok

elif(zadanie == 9):
    side = int(input("Podaj bok pustego kwadratu  : "))


    for i in range(side):
        for j in range(side):
            if (i == 0 or i == side - 1 or j == 0 or j == side - 1):
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()


#petla od 100 do 0 co 10, w sensie ze w dol jedzie

elif(zadanie == 10):
    for i in range(100, -1, -10):
        print(str(i))


#petla while
#https://www.w3schools.com/python/python_while_loops.asp


