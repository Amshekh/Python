# We are going to find volume of right circular cone by passing values through object inside function defined in class
# Receiving values inside function through object and perform task
"""
class Rcir_cone():
    def Vol(self, r, h):  # Two parameters which will receive the values passed by arguments in object
        pi = 22 / 7
        self.r = r    # Syntax: self followe by dot and then variable name and  assign it to variable name
        self.h = h
        v = 1 / 3 * pi * r * r * h
        print("Volume of right circular cone with entered radius and height is:", v)

obj = Rcir_cone()   # Here we have created an object of class Rcir_cone
r = int(input("Enter the radius:"))
h = int(input("Enter the height:"))
obj.Vol(r, h) # object name followed by dot and then function name and inside we mention two inputs 

"""

# Alternatively you can also print like this

class Rcir_cone():
    def Vol(self, r, h):  # Two parameters which will receive the values passed by arguments in object
        pi = 22 / 7
        self.r = r    # Syntax: self followe by dot and then variable name and  assign it to variable name
        self.h = h
        v = 1 / 3 * pi * r * r * h
        return v  # We have to return this v  after calculation, so that it can be print there
        

obj = Rcir_cone()   # Here we have created an object of class Rcir_cone
r = int(input("Enter the radius:"))
h = int(input("Enter the height:"))
print("Volume of right circular cone with entered radius and height is:",obj.Vol(r, h))