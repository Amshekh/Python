size = int(input("Enter the size of the array : "))
print("Enter the elements of the array with size", size)

array = []
for i in range(size):
    array.append(int(input()))
print("Initial array is :", array)

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2 # if number of elements in array is odd then yo will take floor value
        left = array[0 : mid]  # left = array[:mid]
        right = array[mid : len(array)] # right = array[mid:]
        print("left : ", left,"\t","right : ", right)

        mergeSort(left)
        mergeSort(right)

        m = n = o = 0

        while m < len(left) and n < len(right):
            if left[m] <= right[n]:
                array[o] = left[m]
                m = m + 1
            else:
                array[o] = right[n]
                n = n + 1
            o = o + 1
    
        while m < len(left):
            array[o] = left[m]
            m = m + 1
            o = o + 1
        while n < len(right):
            array[o] = right[n]
            n = n + 1
            o = 0 + 1
        print(array)
mergeSort(array)    
print("Resultant Sorted array after applying Merge Sort is :", array)