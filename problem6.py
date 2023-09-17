age=eval(input("Enter your age:"))
if age<0:
    print("Invalid input!")
else:
    if age>=0 and age<=3:
        print("Ticket is Free!")
    elif age>=4 and age<12:
        print("Cost of Ticket is 10$")
    elif age>=12 and age<=15:
        print("Cost of Ticket is 15$")
    else:
        print("Cost of Ticket is 20$")