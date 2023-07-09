size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is :", array)
x = int(input(("Enter the element to be searched : ")))

def binarySearch(array, x):
    low = 0
    high = len(array) - 1

    while (low <= high and low != -1):
        mid = (low + high) // 2  # use floor value if array length is odd number

        if array[mid] == x:
            return mid
        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

result = binarySearch(array, x) # as index in array starts from 0, 1, ... so on

if result == -1:
    print("There is no such element in the array")
else:
    print("Element found at the index :", result) # indexing in array starts from 0, 1, 2, ...so on
