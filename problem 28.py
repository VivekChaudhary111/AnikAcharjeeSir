'''
Assignmen 28: Largest of two numbers
   num1 num2
1-> 4    0 (invalid)
2-> 0    4 (invalid)
3-> 0    0 (invalid)
4-> -1   -2 (invalid)
5-> 0.4   0.5 (invalid)
6-> 15   5  (valid) 15 is the largest and 5 is the smallest
7-> 5    15 (valid) 5 is the smallest and 15 is the largest
8-> 4    4  (valid) (both numbers are same)
'''
num1=eval(input("num1:"))
num2=eval(input("num2:"))
if num1<1 or num2<1:
    print("Invalid!")
elif num1>num2:
    print(f"{num1} is largest and {num2} is smallest")
elif num1<num2:
    print(f"{num1} is smallest and {num2} is largest")
else:
    print("Both numbers are same")
    