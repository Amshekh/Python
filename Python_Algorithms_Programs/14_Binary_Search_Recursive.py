size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is :", array)
x = int(input(("Enter the element to be searched : ")))

def binarySearch(array, x, low, high):

    while(high >= low and low != -1):
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)
        else:
            return binarySearch(array, x, mid + 1, high)
    return -1
    
result = binarySearch(array, x, 0, len(array) - 1)

if result == -1:
    print("There is no such element in the array")
else:
    print("Element found at the index :", result)
