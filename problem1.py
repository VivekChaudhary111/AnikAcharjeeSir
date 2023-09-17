#Problem: Write a program that takes two numbers as input from the user amd performs basic arithmetic
#operations (addition, subtraction, multiplication, division) on them.

num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

#simple

addition= num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
print(addition,subtraction,multiplication,division)

#Formatted Strings

print(f"The sum is:{num1 + num2}")
print(f"The subtraction is:{num1 - num2}")
print(f"The multiplicarion is:{num1 * num2}")
print(f"The division is:{num1 / num2}")
