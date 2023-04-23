def hex_to_decimal(hexa):
    # Check if the input is a hexadecimal string
    if not all(char in '0123456789ABCDEFabcdef' for char in hexa):
        return "Invalid input"
    
    # Initialize variables
    decimal = 0
    power = len(hexa) - 1
    
    # Define the mapping of hex digits to decimal values
    hex_map = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }
    
    # Convert hex to decimal using powers of 16
    for digit in hexa:
        decimal += hex_map[digit.upper()] * (16 ** power)
        power -= 1
    
    return decimal



hex=input('Podaj liczbe w systemie szesnastkowym: ')
dec=hex_to_decimal(hex)
print('Liczba w systemie dziesietnym to: ')
print(dec)