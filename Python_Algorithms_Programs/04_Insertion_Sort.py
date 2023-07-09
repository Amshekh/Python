size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))

print("\n")
print("Initial array is : ", array)

for m in range(1, size):
    n = m
    while n > 0 and array[n] < array[n - 1]:
        array[n - 1], array[n] = array[n], array[n - 1]
        n = n - 1
        print("\n")
        print(array)

print("\n")
print("The sorted array after applying Insertion Sort is : ", array)
