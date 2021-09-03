ToDo=list()
Done=list()
print("************************************")
print("To Add New Item Press 1")
print("To Print the To Do List Press 2")
print("To Mark an item as Done Press 3")
print("To Print the Done list Press 4")
print("************************************")
i=1
while i > 0 :
	choice=input("Please enter your choice: ")
	if choice == '1':
		item=input("Please Enter Item to add: ")
		ToDo.append(item)
		print("Thank you, Item added successfully.")
	elif choice == '2':
		print(ToDo)
	elif choice == '3':
		index=input("Please enter item index : ")
		index=int(index)
		DoneItem=ToDo.pop(index)
		Done.append(DoneItem)
		print("Thank you, Item added successfully.")
	elif choice == '4':
		print(Done)
	else:
		print("Wrong Choice, Please Try Again.")
	i+=1