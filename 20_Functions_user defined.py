# user defined function to calculate percentage
n = input("Enter your name: ")
roll = int(input("Enter your 7 digit roll number:"))

def perc_function(tot): # tot is the parameter
    perc = tot/300 * 100
    return perc
    
    
q = int(input("Enter your Quantitative Aptitude marks:"))
r = int(input("Enter your Reasoning marks:"))
e = int(input("Enter your English marks:"))
tot = sum((q,r,e)) # sum is a built-in function of python
result = perc_function(tot)  # calling the function, here tot is the argument
# print("Candidate",n,"whose roll no. is",roll,"has obtained",result,"percentage of marks")
print("Candidate",n,"whose roll no. is",roll,"has obtained",round(result,2),"percentage of marks") # round will round off percentage to two places of decimal

    
    
 