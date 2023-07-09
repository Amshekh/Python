# Class is a "blueprint" for creating objects. An object is a real world entity.
# Almost everything in Python is an object, with its properties and methods.
# When a class is defined, no memory is allocated but when an object is created memory is created

class Employee_Details:
    def printDetails(self):  # While using functions in Python for OOP's concept, it's necessary to write  (self).Here self is aparameter
        print("Employee Id:", self.eid)
        print("Employee Name:", self.ename)
        print("Company name:", self.ecomp)
        print("Emoloyee post:", self.epost)
        print("Employee CTC(which includes stocks):", self.ectc)
        print("Employee location:", self.eloc)

Amit = Employee_Details()      # object creation. Syntax:  object name = classname()        

Amit.eid = "99988007"
Amit.ename = "Amit Shekhar"
Amit.ecomp = "ColradoSoft Technologies"
Amit.epost = "Data Scientist/Data Engineer"
Amit.ectc = "185000 usd"
Amit.eloc = "Colrado, usa"

Amit.printDetails()

# In simple terms you can understand like this: class  is like a form  and the person filling that form is the  object.
