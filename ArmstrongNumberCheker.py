'''
Problem:Build a program that checks if a given number is Armstrong number 
(a number that is equal to the sum of its own digits each raised to the power of the number of the digits).
For Example: 3**3 +7**3 +1**3=371.

'''
#if (eval(num[0]))**len(num) + (eval(num[1]))**len(num) + (eval(num[2]))**len(num)==a:
   # print("The given number is a Armstrong Number.")

num=str(input("Enter the number to be checked:"))
a=0
for i in range(len(num)):
    a+=(eval(num[i]))**len((num))
    print(a)
if a==eval(num):
    print("The given number is a Armstrong Number.")
else:
    print("The given number is not a Armstrong Number.")    
    
   

  




