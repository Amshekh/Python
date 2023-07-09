# Modules in Python
# Module is a file containing functions which can be imported and used in our programs
# We can use module by using 2 methods  (i) Pre created module   (ii) Module created by Us
# Now Pre created modules are of 2 types  (i) Built in module (pre installed in python)  | (ii) External modules (one has to install before using it)

import time  # Syntax: import keyword followed by module name  | time is a built-in module and we need to use import before using it

today = time.asctime(time.localtime(time.time()))
print("Today is",today,"\n")

# to print calender of entered year and month
import calendar

y = int(input("Enter the year: "))
m = int(input("Enter the month: "))

cal = calendar.month(y, m)
print("\n",cal)
