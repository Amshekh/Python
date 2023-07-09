size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size :", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is :", array)
x = int(input("Enter the element to be searched in this array : "))
l = len(array)

def linearSearch(array, l, x):
    for m in range(0, l):
        if (array[m] == x):
            return m
    return -1
    
result = linearSearch(array, l, x)

if result == -1:
    print("There is no such element in the array")
else:
    print("Element found at the index :", result)
