end=int(input("Enter the end Natural no.:"))
sum_even=0
for i in range(2,end+1,2):
    sum_even+=i
print(f"sum of even no. is{sum_even}")
sum_odd=0
for r in range(1,end+1,2):
    sum_odd+=r
print(f"sum of odd no. is{sum_odd}")
