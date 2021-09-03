def SET_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR | (1 << BIT)
	return result
	
def CLR_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR & (~(1 << BIT))
	return result
	
def GET_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = (VAR >> BIT) & 1
	return result
	
def TOG_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = (1 << BIT) ^ VAR
	return result