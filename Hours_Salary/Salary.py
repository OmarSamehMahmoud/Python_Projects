x=input("Please Enter the emolyee name")
y=input("Please Enter no. of hours")
y=int(y)
if x == "Ahmed" or "Ali" :
	if y >= 40 :
		Salary = y * 100  
		Salary=str(Salary)
		print("Your montly salary is "+Salary)
	else:
		Salary = y * 100
		DecSalary = Salary * (10/100)
		reSalary=Salary-DecSalary
		DecSalary=str(DecSalary)
		reSalary=str(reSalary)
		print("Your montly salary is "+reSalary)
		print("Your Dudction is "+DecSalary)
elif x == "Amr" or "Andrew" :
	if y >= 40 :
		Salary = y * 80  
		Salary=str(Salary)
		print("Your montly salary is "+Salary)
	else:
		Salary = y * 80
		DecSalary = Salary * (10/100)
		reSalary=Salary-DecSalary
		DecSalary=str(DecSalary)
		reSalary=str(reSalary)
		print("Your montly salary is "+reSalary)
		print("Your Dudction is "+DecSalary)
elif x == "Aya"  :
	if y >= 40 :
		Salary = y * 60  
		Salary=str(Salary)
		print("Your montly salary is "+Salary)
	else:
		Salary = y * 60 
		DecSalary = Salary * (10/100)
		reSalary=Salary-DecSalary
		DecSalary=str(DecSalary)
		reSalary=str(reSalary)
		print("Your montly salary is "+reSalary)
		print("Your Dudction is "+DecSalary)
else :
	pass