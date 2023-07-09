size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is : ", array)

def heapify(array, size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < size and array[i] < array[l]:
        largest = l

    if r < size and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, size, largest)

def heapSort(array):
    for m in range(size // 2 - 1, -1, -1):
        heapify(array, size, m)

    for m in range(size - 1, 0, -1):
        array[m], array[0] = array[0], array[m]

        heapify(array, m, 0)

heapSort(array)

print("Resultant array after applying Heap Sort is :", array)
