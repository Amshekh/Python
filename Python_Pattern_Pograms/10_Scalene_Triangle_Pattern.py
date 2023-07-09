r = int(input("Enter number of rows : "))

spaces = r - 1

for m in range(r):
    for n in range(spaces):
        print(end=" ")

    spaces = spaces - 1
    for n in range(m + 1):
        print("*", end="  ")
    print()
