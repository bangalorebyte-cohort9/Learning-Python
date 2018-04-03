
class Number:

	def __init__(self,start):
		self.data = start
        
	def __add__(self,value):
		return Number(self.data + value.data)

	def __sub__(self,value):
		return(self.data - value.data)
    
	def __str__(self):
		return (str(self.data))


x = Number(10)
y = Number(20)
w = Number(30)

z = x+y+w

print(type(z.data))

print(type(str(z)))
