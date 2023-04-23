def decimal_to_binary(decimal):
    # Check if the input is a positive integer
    if decimal < 0 or int(decimal) != decimal:
        return "Invalid input"
    
    # Initialize variables
    binary = ''
    quotient = decimal
    
    # Convert decimal to binary by dividing by 2 and appending remainder
    while quotient != 0:
        remainder = quotient % 2
        binary = str(remainder) + binary
        quotient = quotient // 2
    
    return binary

# Example usage
decimal = int(input('Podaj liczbe dziesietna: '))
binary = decimal_to_binary(decimal)
print(binary) # prints '101010'
