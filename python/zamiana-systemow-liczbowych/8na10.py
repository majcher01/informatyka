def octal_to_decimal(octal):
    # Check if the input is an octal string
    if not all(char in '01234567' for char in octal):
        return "Invalid input"
    
    # Initialize variables
    decimal = 0
    power = len(octal) - 1
    
    # Convert octal to decimal using powers of 8
    for digit in octal:
        decimal += int(digit) * (8 ** power)
        power -= 1
    
    return decimal



oct=input('Podaj liczbe w systemie osemkowym: ')
dec=octal_to_decimal(oct)
print('Liczba w systemie dziesietnym to: ')
print(dec)