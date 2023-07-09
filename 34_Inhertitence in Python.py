# The class which inherits the parent class will have all the features of the parent class  |  Reusability

class EmpPersonal_Info():
    def print_Details(self):
        print(f"Employee ID : {self.empID}  Employee Name : {self.empName}  Gender : {self.empGender}  Company Name : {self.empComp}  Employee Post : {self.empPost}  CTC(including company stocks): {self.empCtc}  Employee Location : {self.empLoc}")
              # f string allows to print multiple values at once 

# class Cost_To_Company(): # Now we will inherit the class EmpPersonal_Info()

class Cost_To_Company(EmpPersonal_Info): # Syntax: just enter the parent class name in round brackets and that class will get inherit
    def Calculate_Ctc(self):
        Per_Day_Salary = self.basic_salary / 30
        Working_Days = 30 - self.leave
        House_Rent_Allowance = 0.35 * self.basic_salary
        Other_Allowances = 0.10 * self.basic_salary
        Income_Tax = 0.33 * self.basic_salary
        E_Provident_Fund = 0.25 * self.basic_salary
        Other_Deductions = 0.05 * self.basic_salary
        Inflation_Allowance_due_to_interest_rate_hike_by_FED = 0.10 * self.basic_salary

        Net_Salary = (Per_Day_Salary * Working_Days) + (House_Rent_Allowance + Other_Allowances + Inflation_Allowance_due_to_interest_rate_hike_by_FED) - (Income_Tax + E_Provident_Fund + Other_Deductions)
        print("Your Net Salary is: ", Net_Salary, "usd")

Employee = Cost_To_Company()    # Object is created     

Employee.basic_salary = 135000
Employee.leave = 2
Employee.empID = 99988007
Employee.empName = "Amit Shekhar"
Employee.empGender = "Male"
Employee.empComp = "ColradoSoft Technologies"
Employee.empPost = "Data Engineer/Data Scientist"
Employee.empCtc = "185000 usd"
Employee.empLoc = "Colrado, usa"


Employee.print_Details()  # calling the function print_Details  from class  EmpPersonal_Info
Employee.Calculate_Ctc()  # calling the function Calculate_Ctc  from  class  Cost_To_Company





