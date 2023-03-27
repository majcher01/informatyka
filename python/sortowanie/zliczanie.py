def counting_sort(arr):
    n = len(arr)
    
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create count arrays to store the count of each element
    count = [0] * (max_element + 1)
    
    # Store the count of each element in the array
    for i in range(n):
        if arr[i] < 0:
            print("==Program nie obsługuje liczb ujemnych==")
            return None
        count[arr[i]] += 1
    
    # Modify the count array to store the position of each element in the sorted array
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create a sorted array
    sorted_arr = [0] * n
    for i in range(n-1, -1, -1):
        sorted_arr[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        
    return sorted_arr

# Get user input
input_str = input("Wprowadź liczby oddzielone spacjami: ")
input_list = [int(num) for num in input_str.split()]

# Sort the list using counting sort
sorted_list = counting_sort(input_list)

# If sorted_list is None, it means that the user entered a negative number
if sorted_list is not None:
    # Print the sorted list
    print("Posortowane liczby:", sorted_list)
