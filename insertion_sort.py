def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = [39, 12, 18, 85, 72, 10, 2, 18]
insertion_sort(arr)
print(arr)
