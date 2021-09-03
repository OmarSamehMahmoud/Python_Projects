x=100
def func():
	global x
	x=200
	y=20
	print(y)
	print(x)
func()
print(x)