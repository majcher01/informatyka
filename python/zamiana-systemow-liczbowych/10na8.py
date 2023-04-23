def decimal_to_octal(decimal):
    # Check if the input is a positive integer
    if decimal < 0 or int(decimal) != decimal:
        return "Invalid input"
    
    # Initialize variables
    octal = ''
    quotient = decimal
    
    # Convert decimal to octal by dividing by 8 and appending remainder
    while quotient != 0:
        remainder = quotient % 8
        octal = str(remainder) + octal
        quotient = quotient // 8
    
    return octal

# Example usage
decimal = int(input('Podaj liczbe dziesietna: '))
octal = decimal_to_octal(decimal)
print(octal) # prints '173'
