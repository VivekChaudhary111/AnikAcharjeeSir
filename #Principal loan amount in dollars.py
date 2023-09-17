#Principal loan amount in dollars
p=int(input("Enter the Principal loan amount in dollars: $ "))
#Annual interest rate(r) in percentage
r=int(input("Enter the Annual interest rate(r)(in percentage) :"))
#Loan term in year(n)
n=int(input("Enter the Loan term (in year) :"))
r=(r/12)/100
n=n*12
M =(p* r * ((1+r)**n))/(((1+r)**n)-1)
#Monthly payment(M) in dollars
print(f"The Monthly payment is: $",round(M,2))
