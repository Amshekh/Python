size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is :", array)

def countingSort(array, place):
    output = [0] * size
    count = [0] * 10

    for m in range(0, size):
        index = array[m] // place
        count[index % 10] += 1

    for m in range(1, 10):
        count[m] += count[m - 1]

    m = size - 1
    while m >= 0:
        index = array[m] // place
        output[count[index % 10] - 1] = array[m]
        count[index % 10] -= 1
        m -= 1

    for m in range(0, size):
        array[m] = output[m]

def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

radixSort(array)

print("Resultant array after applying Radix Sort is :", array)