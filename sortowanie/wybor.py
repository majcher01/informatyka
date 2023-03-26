def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Get user input for the list of numbers
numbers = input("Wprowadź liczby oddzielone spacją: ").split()
numbers = [int(num) for num in numbers]

# Sort the numbers using selection sort
sorted_numbers = selection_sort(numbers)
print("Posortowane liczby: ")
print(sorted_numbers)
