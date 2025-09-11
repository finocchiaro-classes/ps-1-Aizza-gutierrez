# So this function should do everything that part 1 did, except we will create a function that does the math
# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
# Repeat back the numbers
  print(f' A:{a} and B:{b}')
  #Perform calculations. Be careful about string formatting for autograders.
  print (int(a) + int(b) )   # this is the addition  
  print (int(a) * int(b) ) # this is the multiplication 
  print (int(a) ** int(b) ) # this is the exponential
  print (int(a) % int(b) ) # this is the modulus   
  
#This part asks the user for the first number, stores the value in a variable
firstnum = input("Enter an integer between 10 and 100") 

# Ask the user for the second number, store the value in a variable
secondnum = input("Enter another integer that is less than 4") 
number_fun(firstnum, secondnum) 
