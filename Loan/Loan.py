x=input("Please Enter the loan value")
x=int(x)
y=input("Please Enter no. of years")
y=int(y)
z=(x+(0.12*x*y))/(y*12)
z=str(z)
print("Your montly installment is "+z)