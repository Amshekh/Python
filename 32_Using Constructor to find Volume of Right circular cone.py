# We will now find Volume of Righr Circular Cone, using constructor in our class

class Rcir_cone():
    def __init__(self, r, h):  # Two parameters which will receive the values passed by arguments in object
        pi = 22 / 7
        self.r = r    # Syntax: self followe by dot and then variable name and  assign it to variable name
        self.h = h
        v = 1 / 3 * pi * r * r * h
        print("Volume of right circular cone with entered radius and height is:", v)

r = int(input("Enter the radius:"))
h = int(input("Enter the height:"))
obj = Rcir_cone(r, h)   # Here we have created an object of class Rcir_cone        

# We don't require to call constructor and it get's called automatically, but in case of function we need to call it.
