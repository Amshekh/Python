r = int(input("Enter number of rows : "))

spaces = (2 * r) - 2

for m in range(r, -1, -1):
    for n in range(spaces, 0, -1):
        print(end=" ")
    spaces = spaces + 1
    for o in range(0, m +1):
        print("*", end=" ")
    print()
