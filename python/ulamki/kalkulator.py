import sys

print("+ = dodawanie")
print('- = odejmowanie')
print('/ - dzielenie')
print('* = mnozenie')


sw=input('wybierz operacje (+,-,/,*): ')
if(sw!="+" and sw!="-" and sw!="/" and sw!="*"):
    print("Nieprawidlowa operacja")
    sys.exit()

print("Podaj ułamki w formacie x/y")
u1=input("Pierwszy: ")
u2=input("Drugi: ")

l1, m1 = u1.split('/')
l2, m2 = u2.split('/')
    
l1=int(l1)
m1=int(m1)
l2=int(l2)
m2=int(m2)

def gcd(a, b):
    # Base case: if b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: find the GCD of b and the remainder of a divided by b
    return gcd(b, a % b)

def lcm(a, b):
    # Compute the LCM using the formula
    lcm = (a * b) // gcd(a, b)

    return lcm

def sf(numerator, denominator):
    # Check if the denominator is 0
    if denominator == 0:
        return None
    
    # Calculate the GCD of the numerator and denominator
    gcd = abs(numerator)
    temp = abs(denominator)
    while temp != 0:
        gcd, temp = temp, gcd % temp
    
    # Simplify the fraction if the GCD is greater than 1
    if gcd > 1:
        numerator //= gcd
        denominator //= gcd
    
    # Return the simplified fraction as a tuple
    return (numerator, denominator)

    
if(sw=="+"):
    wspolny=lcm(m1, m2)
    l1=l1*(wspolny/m1)
    l2=l2*(wspolny/m2)
    
    #print('ws: ',wspolny," l1m: ",l1," l2m: ",l2)
    lw=l1+l2
    lw=int(lw)
    
    sk=sf(lw, wspolny)
    
    if sk is not None:
        wynik=str(sk[0])+"/"+str(sk[1])
        print(wynik)
    else:
        wynik=str(lw)+"/"+str(wspolny)
        print("Wynik: ",wynik)
    
if(sw=="-"):
    wspolny=lcm(m1, m2)
    l1=l1*(wspolny/m1)
    l2=l2*(wspolny/m2)
    
    #print('ws: ',wspolny," l1m: ",l1," l2m: ",l2)
    lw=l1-l2
    lw=int(lw)
    
    sk=sf(lw, wspolny)
    
    if sk is not None:
        wynik=str(sk[0])+"/"+str(sk[1])
        print(wynik)
    else:
        wynik=str(lw)+"/"+str(wspolny)
        print("Wynik: ",wynik)
        
if(sw=="/"):
    
    lw=l1*m2
    wspolny=m1*l2
    lw=int(lw)
    wspolny=int(wspolny)
    
    sk=sf(lw, wspolny)
    
    if sk is not None:
        wynik=str(sk[0])+"/"+str(sk[1])
        print(wynik)
    else:
        wynik=str(lw)+"/"+str(wspolny)
        print("Wynik: ",wynik)
        
        
if(sw=="*"):
    
    lw=l1*l2
    wspolny=m1*m2
    lw=int(lw)
    wspolny=int(wspolny)
    
    sk=sf(lw, wspolny)
    
    if sk is not None:
        wynik=str(sk[0])+"/"+str(sk[1])
        print(wynik)
    else:
        wynik=str(lw)+"/"+str(wspolny)
        print("Wynik: ",wynik)