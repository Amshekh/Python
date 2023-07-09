# to replace string in Python
x = "Data Scientist"
y = (x.replace("Data", "Applied"))  # now Data will be replaced by Applied
print("After replacing the new string is: ",y)

# To split string in Python
z = (x.split())
print("After using split method output is: ",z)

# To capitalize first letter of string 
s = "hakuna matata"
res = (s.capitalize())
print("Desired output after using capitalize method is: ", res)

# To print string to a derired width on code screen/ output screen/ terminal
c = (s.center(75))  # we want string content in s to print on with width from initial position to 75px
print("Desired output after using center method is: ",c)

# To check a string ends with particular letter/letters
e = (s.endswith("ta"))
print("Whether string <hakuna matata> ends with ta? ",e)  # Here e will have value stored as True because hakuna matata ends with ta

# To find position of a particular string
f = (s.find("un"))
print("The position is: ", f)  # counting starts from 0,1,2,3,4....so on

# To find index of paricular letter in the string
i = (s.index("n"))
print("The index of letter n in string <hakuna matata> is: ",i)

# to find if the content in variable is alphabetical or not
w = "Gideon"
o = (w.isalpha())
print("Whether <Gideon> is a string?",o)

# to find if the content in variable is numerical or not
n = "71354"
r = (n.isdigit())
print("Whether <71354> is string?",r)

# to check whether the variable declared is empty or not
m = (w.isspace()) # here w is filled with Gideon, so it will return false
print(m)

# to check whether the first word of the string is capital or not
g = (w.istitle()) # As first letter of word Gideon is capital,it will return true
print(g)

# to count a particular word in a sentence
sent = "the quick brown fox jumps over the lazy dog"
n = (sent.count("the")) # the word comes two times in the sentence, so output is 2
print(n)

# to add a paticular character (e.g. *, /, _, #  etc) in list of strings
list = ["Emma", "Elizabeth", "Ana", "Margot", "Kate"]
h = "*".join(list) # All elements of list will be joined by *
print(h)
j = " ".join(list) # All elements of list will now have space between them
print(j)

