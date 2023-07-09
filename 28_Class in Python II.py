# Variable creation in class and discuss about instance variable priority 
class Employee_Details:
    company_name = "ColaradoSoft Technologies"
    def printDetails(self):  # While using functions in Python for OOP's concept, it's necessary to write  (self).Here self is aparameter
        print("Employee Id:", self.eid)
        print("Employee Name:", self.ename)
        print("Emoloyee post:", self.epost)
        print("Employee CTC(which includes stocks):", self.ectc)
        print("Employee location:", self.eloc)

Amit = Employee_Details()      # object creation. Syntax:  object name = classname()        

Amit.eid = "99988007"
Amit.ename = "Amit Shekhar"
Amit.epost = "Data Scientist/Data Engineer"
Amit.ectc = "185000 usd"
Amit.eloc = "Colrado, usa"

Amit.printDetails()

Amit.company_name = "BritSoft Technologies" # when an object creates its own instance variable, then priority is given to it and not instance variable created inside class
print("Company name:",Amit.company_name)  # Now company name will be printed as BritSoft Technologies and not ColradoSoft Technologies

# However if we comment the above line where we have given company name as BritSoft Technologies, then company name will be print as ColradoSoft Technologies