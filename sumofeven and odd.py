start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
sum_even=0
sum_odd=0
for num in range(start,end+1):
    if num%2==0:
        sum_even+=num
    else:
        sum_odd+=num
print(f"The sum of even no, between {start} and{end} is {sum_even}")
print(f"The sum of odd no, between {start} and{end} is {sum_odd}")

    
