def binary_to_decimal(binary):
    # Check if the input is a binary string
    if not all(char in '01' for char in binary):
        return "Invalid input"
    
    # Initialize variables
    decimal = 0
    power = len(binary) - 1
    
    # Convert binary to decimal using powers of 2
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    
    return decimal

bin=input('Podaj liczbe w systemie dwojkowym: ')
dec=binary_to_decimal(bin)
print('Liczba w systemie dziesietnym to: ')
print(dec)