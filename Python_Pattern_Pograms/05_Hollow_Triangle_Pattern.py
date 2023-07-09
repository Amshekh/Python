r = int(input("Enter number of rows : "))

for m in range(1, r+1):
    for n in range(m):
        if n == 0 or n == m -1:
            print("*", end=" ")
        elif m != r:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()