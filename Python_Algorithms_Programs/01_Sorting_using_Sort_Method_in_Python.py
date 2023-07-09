size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size ", size)

array = []
for i in range(size):
    array.append(int(input()))

array.sort()

print("The sorted array in ascending order is : ", array, "\n")

array.sort(reverse = True)

print("The sorted array in descending order is : ", array)