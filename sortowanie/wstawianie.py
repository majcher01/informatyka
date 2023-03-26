def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
    return arr

# Get user input for the list of numbers
numbers = input("Wprowadź liczby oddzielone spacją: ").split()
numbers = [int(num) for num in numbers]

# Sort the numbers using insertion sort
sorted_numbers = insertion_sort(numbers)
print("Posortowane liczby: ")
print(sorted_numbers)
