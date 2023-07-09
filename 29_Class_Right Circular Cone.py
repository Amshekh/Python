# Class to find volume of Right circular Cone
class Rcir_cone():
    def Vol(self):
        pi = 22 / 7
        r = int(input("Enter the radius:"))
        h = int(input("Enter the height:"))
        v = 1 / 3 * pi * r * r * h    # volume of right cicular cone is  (1/3)*(22/7)*r*r*h
        print("Volume of right circular cone with entered radius and height is:", v)

obj = Rcir_cone()   # Here we have created an object of class Rcir_cone

obj.Vol()
