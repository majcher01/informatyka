def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    min_value, max_value = min(arr), max(arr)
    
    bucket_count = (max_value - min_value) // bucket_size + 1
    
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)
        
    for i in range(bucket_count):
        buckets[i].sort()
        
    result = []
    for bucket in buckets:
        result.extend(bucket)
        
    return result

numbers = input("Wprowadź liczby oddzielone spacją: ").split()
numbers = [int(num) for num in numbers]

sorted_numbers = bucket_sort(numbers)
print("Posortowane liczby: ")
print(sorted_numbers)
