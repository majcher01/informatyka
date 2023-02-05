def main():
    N = [200, 100, 50, 20, 10, 5, 2, 1]
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
