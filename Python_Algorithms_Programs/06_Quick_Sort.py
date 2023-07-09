size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))
print("Initial array is :", array)

def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)

def partition(arr, left, right):
    m = left
    n = right - 1
    pivot = arr[right]
    print("Pivot ", pivot)
    while m < n:
        while m < right and arr[m] < pivot:
            m = m + 1
            print("m", m, "\t", "arr[m]", arr[m])

        while n > left and arr[n] >= pivot:
            n = n -1
            print("n", n, "\t", "arr[n]", arr[n])

        if m < n:
            arr[m], arr[n] = arr[n], arr[m]
            print(arr)
    if arr[m] > pivot:
        arr[m], arr[right] = arr[right], arr[m]
        print(arr)
    return m

quickSort(array, 0, size - 1) # quickSort(array, 0, size - 1) will also work

print("Resultant array after applying Quick Sort is :", array)