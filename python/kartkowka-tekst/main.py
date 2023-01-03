##zadanie 1

liczbausmiechow=int(input('podaj liczbe usmiechow '))

def usmiechy(liczba):
    print(':)'*liczba)

usmiechy(liczbausmiechow)


napis1='mmaakkdat'
napis2='jjuulma'




def policz(g):
    count = 0
    for i in range(len(g) -1):
        if g[i] == g[i+1]:
            count+=1
    return count


print(policz(napis1))
print (policz(napis2))



##zadanie 3
napis3='kartka papieru'
napis4='kartka bloku'

napis3_2=napis3.replace("kartka", "Rolka")
napis4_2=napis4.replace("kartka", "Rolka")

print(napis3_2 + ' ' + napis4_2)
