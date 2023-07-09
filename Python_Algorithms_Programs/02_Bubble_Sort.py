import numpy as npy

size = int(input("Enter the size of array : "))
print("Enter elements for array with size", size)
array = []
for i in range(size):
    array.append(int(input()))

array = npy.array(array)

for m in range(0, size):
    for n in range(0, size - m - 1):
        if array[n] > array[n + 1]:
            temp = array[n]
            array[n] = array[n + 1]
            array[n + 1] = temp
print("Resultant array after applying bubble sort is ", array)
