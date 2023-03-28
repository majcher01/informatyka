print("1.Sortowanie kubełkowe.")
print("2.Sortowanie przez wstawianie.")
print("3.Sortowanie przez wybór.")
wybor=int(input('Wybierz zadanie: (1-3): '))

if(wybor==1):

        
    def bucket_sort(arr, bucket_size=10):
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

    T=[2,3,4,14,23,35,22,6,8,1]
    sorted_numbers = bucket_sort(T)
    print("Posortowane liczby: ")
    print(sorted_numbers)
elif(wybor==2):
    
    def insertion_sort(arr):
        n = len(arr)
    
        for i in range(1, n):
            key = arr[i]
 
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1] = key
        
        return arr

    T=[8,1,4,2,0,11]
    print("Liczby przed sortowaniem: ")
    print(T)
    sorted_numbers = insertion_sort(T)
    print("Posortowane liczby: ")
    print(sorted_numbers)
elif(wybor==3):

    def selection_sort(arr):
        n = len(arr)
    
        for i in range(n):
        
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
                
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr

    T = input("Wprowadź liczby oddzielone spacją: ").split()
    T = [int(num) for num in T]

    print("Liczby przed sortowaniem: ")
    print(T)
    sorted_numbers = selection_sort(T)
    print("Posortowane liczby: ")
    print(sorted_numbers)
else:
    print("niepoprawny numer zadania")