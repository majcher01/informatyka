u1=input("Podaj ułamek w formacie x/y: ")

l1, m1 =u1.split("/")

l1=int(l1)
m1=int(m1)




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



sk=sf(l1, m1)
    
if sk is not None:
    wynik=str(sk[0])+"/"+str(sk[1])
    print(wynik)
else:
    wynik=str(lw)+"/"+str(wspolny)
    print("Wynik: ",wynik)
