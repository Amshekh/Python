# Simple calculator using constructor and functions

class Calculator():
    def __init__(self, x, y): # As constructor gets called automatically, we will utilize it in passing values
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
    def mod(self):
        return self.x % self.y

x = int(input("Enter the first no :"))
y = int(input("Enter the second no :"))
print("\n")

obj = Calculator(x, y) # Now since we are using constructor, we don't require to call it and arguments will be passed automatically

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Divison")
    print("5. Modulus")

    print("\n")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Result =", obj.add())
    elif choice == 2:
        print("Result =", obj.sub())
    elif choice == 3:
        print("Result =", obj.mul())
    elif choice == 4:
        print("Result =", round(obj.div(), 2))
    elif choice == 5:
        print("Result =", obj.mod())
    elif choice == 0:
        print("Exiting...", "Goodbye!")
    else:
        print("Invalid choice!", "Goodbye!")