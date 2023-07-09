size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size ", size)

array = []
for i in range(size):
    array.append(int(input()))

print("Initial array is : ", array)

def shellSort(array):
    gap = len(array) // 2  # Shell Sort follows sequence of N/2, N/4, ..., 1 where N is the number of elements in array
    while gap > 0:
        for m in range(gap, len(array)):
            temp = array[m]
            n = m
            while n >= gap and array[n - gap] > temp:
                array[n] = array[n - gap]
                n = n - gap
            array[n] = temp
            
        gap = gap // 2  # In next iteration, new gap will be twice of previous case. Also // gives floor value in case number of elements in array are odd
    return array

shellSort(array)

print("Resultant array after applying Shell Short is : ", array)
