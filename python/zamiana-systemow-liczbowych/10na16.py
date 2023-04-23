def decimal_to_hex(decimal):
    # Check if the input is a positive integer
    if decimal < 0 or int(decimal) != decimal:
        return "Invalid input"
    
    # Initialize variables
    hexa = ''
    quotient = decimal
    
    # Define the mapping of decimal digits to hex digits
    hex_digits = "0123456789ABCDEF"
    
    # Convert decimal to hex by dividing by 16 and appending remainder
    while quotient != 0:
        remainder = quotient % 16
        hexa = hex_digits[remainder] + hexa
        quotient = quotient // 16
    
    return hexa

# Example usage
decimal = int(input('Podaj liczbe dziesietna: '))
hexa = decimal_to_hex(decimal)
print(hexa) # prints '1C8'
