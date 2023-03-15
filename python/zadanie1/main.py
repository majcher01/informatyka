liczba=int(input("Podaj liczbę: "))

for i in range(1, liczba+1):
   if(i%2==0):
       print("*", end='')
   else:
       print("/", end='')

print("\n")