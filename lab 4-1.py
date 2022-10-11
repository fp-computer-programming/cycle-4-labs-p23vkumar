#1. Create a Python file named lab_4-1.py
#*** You must write a comment for every chunk of code you write from now on***
#2. Prompt the user to enter their first name and store it with an appropriate variable.
#3. Prompt the user to enter their last name and store it with an appropriate variable.
#4. Create a new variable for the user's full name and set it equal to the first 
# name variable plus the last name variable. What is the result?
#5. Is there an issue with this output? How could we fix that?

#print statement for fun to display output 
print("Welcome. Machine operating at 37% efficiency")

#I prompted the user to enter their first name
# I stored it with an appropriate variable.
#The variable stored is Omega for inputing the first name
Omega = input("Enter First Name: ")

#I prompted the user to enter their last name 
# and store it with an appropriate variable.
#The variable stored is Delta for inputing the last name
Delta = input("Enter Last Name: ")

#I created a new variable for the user's full name 
#I Set it equal to the first
Beta = Omega + " " + Delta 
#I printed the statement to display the output of 
#Beta
print("Welcome" + " " + Beta)
#5. Is there an issue with this output? How could we fix that?
print("There was no issue with the output now that there is a space between the first and last name. When you enter the plus and quotes for space, it allows the first and last name to be seperated into two words")