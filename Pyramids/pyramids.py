height = input("Please enter pyramid Hieght: ")
height = int(height)

row = 0
while row < height:
	NumOfSpace  = height - row - 1
	NumOfStars  = ((row + 1) * 2) - 1
	string = ""
	#Step 1: Get the spaces
	i = 0
	while i < NumOfSpace:
		string = string + " "
		i += 1
	
	#step 2: Get the stars
	i = 0
	while i < NumOfStars:
		string = string + "*"
		i +=1
		
	print(string)
	row += 1