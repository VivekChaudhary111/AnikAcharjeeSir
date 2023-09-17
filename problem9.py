side1=eval(input("Side1 of triangle:"))
side2=eval(input("Side2 of triangle:"))
side3=eval(input("Side3 of triangle:"))
if side1<=0 or side2<=0 or side3<0:
    print("Invalid!")
else:
    if side1==side2 and side2==side3:
        print("The given sides are of Equilateral Triangle.")
    elif side1==side2 or side1==side3 or side2==side3:
        print("The given sides are of isosceles Triangle.")
    else:
        print("The given sides are of scalene Triangle.")


