from BIT_MATH import SET_BIT
from BIT_MATH import CLR_BIT
from BIT_MATH import GET_BIT
from BIT_MATH import TOG_BIT

x=1

y=SET_BIT(1,x)
print(y)
y=CLR_BIT(0,x)
print(y)
y=GET_BIT(2,x)
print(y)
y=TOG_BIT(0,x)
print(y)