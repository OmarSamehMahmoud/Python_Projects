Database=dict()

while 1 :
	print("********************************")
	print("To Add New Empolyee Press 1")
	print("To remove Empolyee Press 2")
	print("To print the Empolyee data Press 3")
	print("To print company data base Press 4")
	print("Press other key to exit")
	print("********************************")
	choice=input("Please enter choice: ")
	choice=int(choice)

	#add empolyee
	if choice == 1 :
		ID = input("Please Enter ID: ")
		ID=int(ID)
			#Search of the ID
		if ID in Database.keys():
				#Search for not existing ID
				Proposed = 0
				while Proposed in Database.keys() :
					Proposed += 1
				#ID is exist
				ID=input("ID is exist, Try again "+ str(Proposed) + " : " )
				ID=int(ID)
		name = input("Please Enter Empolyee Name: ")
		salary = input("Please Enter Salary: ")
		
		#Database[ID] = [name,salary]
		#or
		Database[ID]=dict({'Name':name,'Salary':salary})
		print("Done")
	
	#remove empolyee
	elif choice == 2 :
		ID = input("Please Enter ID: ")
		ID=int(ID)
		
		if ID in Database :
			removed = Database.pop(ID)
			print(str(removed['Name'])+" is removed from data base ")
		else : 
			print("Empolyee not found ")
			
	#print empolyee data
	elif choice == 3 :
			ID = input("Please Enter ID: ")
			ID = int(ID)
			if ID in Database:
				print("Empolyee name : "+ str(Database[ID]['Name']))
				print("Empolyee name : "+ str(Database[ID]['Salary']))
			else :
				print("Empolyee is not exist ")

	#print company data
	elif choice == 4 :
		for x in Database :
			print("************* Empolyee"+str(x)+" ************* ")
			print("Empolyee name : "+ str(Database[x]['Name']))
			print("Empolyee name : "+ str(Database[x]['Salary']))
	else:
		print("Thank you,see you later")
		exit()