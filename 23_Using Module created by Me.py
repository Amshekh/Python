# using module created by me   i.e.  My_Module_01.py   in this program

import My_Module_01
# We can also shorten the name of module    by using  as  keyword
# import My_Module_01 as mymod   # Here Mu_Module_01  is  enamed as mymod | Useful when actual module name is large
x = float(input("Enter the first value: "))
print("\n")

res1 = My_Module_01.areasqr(x)
res2 = My_Module_01.areacir(x)

print("Area of Square with entered value is:",res1,"\n")
print("Area of Circle with entered value is:",res2,"\n")

# Here onwards we will require another set of value to calculate area
y = float(input("Enter the second value:"))
print("\n")
res3 = My_Module_01.arearect(x,y)
res4 = My_Module_01.areatri(x,y)
res5 = My_Module_01.areaparall(x,y)

print("Area of Rectangle with entered value is:",res3,"\n")
print("Area of Triangle with entered value is:",res4,"\n")
print("Area of Parallelogram with entered value is:",res5,"\n")