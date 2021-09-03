f=open("file.txt","w+")
i=0
DDR=""
while i < 8 :
	i=str(i)
	x = input("Please enter Bit"+i+"mode : ")
	
	if x == "input" :
		DDR=DDR+"0"
	elif x == "output" :
		DDR=DDR+"1"
	i=int(i)
	i+=1
DDR=str(DDR)
DDRA="DDRA=0b"+DDR
f.write(DDRA)
f.close()