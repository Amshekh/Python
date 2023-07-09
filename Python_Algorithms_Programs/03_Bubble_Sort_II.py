size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size ", size)

array = []
for i in range(size):
    array.append(int(input()))

for m in range(size):
    for n in range(0, size - m - 1):
        print("\n")
        print("n", n)
        print("n+1", n + 1)
        print(array, "\n")
        if array[n] > array[n + 1]:
            array[n], array[n + 1] = array[n + 1], array[n]
            print(array)

print("Resultant array after applying bubble sort is ", array)