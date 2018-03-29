class Person:
    
    def __init__(self,firstname,lastname):
        self.firstname =  firstname
        self.lastname = lastname
    
    
    def printname(self):
        print(self.firstname + ' ' + self.lastname)


class classname:
    
    def __init__(self,arg):
        self.a = arg
        
    def printvalue(self):
        print(self.a)
        

P = Person('Byte', 'Academy')
Q = Person('Acad', 'Gild')

P.printname()
Q.printname()

C = classname(10)
D = classname(20)

C.printvalue()
C.printname()
