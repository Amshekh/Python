size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))
print("Initial array is : ", array)

def selSort(array):
    for m in range(len(array)):  # for m in range(size):  also works fine
        min_element = m
        for n in range(m + 1, len(array)):
            if array[n] < array[min_element]:
                min_element = n
                
        temp = array[m]
        array[m] = array[min_element]
        array[min_element] = temp
        print(array)
    return array

selSort(array)

print("Resultant array after applying Selection Sort is : ", array)
