def merge_sort(arr):
    # If the array has only one element or is empty, return it
    if len(arr) <= 1:
        return arr
    
    # Find the midpoint of the array
    mid = len(arr) // 2
    
    # Recursively sort the left and right halves of the array
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted left and right halves into a sorted array
    sorted_arr = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    
    return sorted_arr

# Get user input
input_str = input("Wprowadź listę liczb oddzielonych spacjami: ")
input_list = [int(num) for num in input_str.split()]

# Sort the list using merge sort
sorted_list = merge_sort(input_list)

# Print the sorted list
print("Posortowana lista:", sorted_list)
