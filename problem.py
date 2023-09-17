'''
To display even and odd numbers between a range
'''
start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
print(f"Even numbers between {start} and {end}:")
for i in range(start,end+1):
    if i %2==0:
        print(i,end=" ")

print(f"\nOdd numbers between {start} and {end}:")
for i in range(start,end+1):
    if i %2!=0:
        print(i,end=" ")




