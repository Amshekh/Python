s = int(input("Enter the size : "))

for m in range(s):
    for n in range(s):
        if m == 0 or m == s-1 or n == 0 or n == s-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()