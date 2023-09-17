# Problem: Build a program that takes the 
# length and width  of a rectangle as input from the
# user and calculates its area.
length=int(input("enter the length:"))
width=int(input("enter the width:"))
print(f"the area of the rectangle is:{length*width}")

#PROBLEM: Create a program that reads the principal amount,interest rate (as a decimal), and time period (in years) from the user,
#and calculates the simple interest using the formula
# simple interest = (Principal * rate * time)/100
principal=int(input("Enter the principal amount:"))
rate=float(input("Enter the interest rate:"))
time=int(input("Enter the time period:"))
print(f"The simple interst = {principal*rate*time/100}")


#PROBLEM: Write a program that takes the user's name as input and then prints a greeting message with their name.
name=input("Enter yor name:")
print(f"Welcome to the GLA University {name}")


#Problem: Write a program that reads the user's birth year and calculates their age.

#Problem: Write a program that reads a time duration in minutes from the user and converts it to hours and minutes.
#For example, 130 minutes should be displayed as "2 hours and 10 minutes".
time_in_minutes=int(input("Enter the time taken in minutes:"))
hours=time_in_minutes//60
remaining_minutes=time_in_minutes%60
print(f"The time taken:{hours} hours and {remaining_minutes} minutes.")

