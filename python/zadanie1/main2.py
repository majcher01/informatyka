from datetime import date
rokurodzenia=int(input("podaj rok urodzenia: "))

rok=date.today().year



def ile_lat(urodzenie):
    print(rok-urodzenie)
    
ile_lat(rokurodzenia)    