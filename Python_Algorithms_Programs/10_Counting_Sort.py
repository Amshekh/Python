size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is :", array)

def countingSort(array):
    output = [0] * size
    count = [0] * 10

    for m in range(0, size):
        count[array[m]] += 1

    for m in range(1, 10):
        count[m] += count[m - 1]

    m = size - 1
    while m >= 0:
        output[count[array[m]] - 1] = array[m]
        count[array[m]] -= 1
        m -= 1

    for m in range(0, size):
        array[m] = output[m]

countingSort(array)

print("Resultant array after applying Counting Sort is :", array)
