#!usr/env/bin python3.6

#numeric operations

"""print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)"""
"""
# operations on Lists
myList = [1,2,3,4]
A = [myList]*3
print(A)
print(myList)
myList[2]=45
print(A)
A[2] = 10
print(myList)
print(A)

# List methods
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

# lists vs string mutability

my_list = [1, 3, True, 6.5]
my_list[0]=2**10

my_string = "Uday"
#my_string[2] = "x"

# Set operations

mySet = {3,6,"cat",4.5,False}
print(mySet)
print(False in mySet)
print("dog" in mySet)

# Set Methods

yourSet = {99,3,100}
newSet  = {1,True,50}
print(mySet.union(yourSet,newSet))
print(mySet | yourSet)

print(mySet.intersection(yourSet,newSet))

# operations on Dictionaries

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)

print(mySet & yourSet)

print(mySet.difference(yourSet))
print(mySet - yourSet)
print({3,100}.issubset(yourSet))

print({3,100}<=yourSet)
mySet.add("house")
print(mySet)
mySet.remove(4.5)
print(mySet)
print(mySet.pop())

print(mySet)
(mySet.clear())
print(mySet)
"""
# Dictionary Methods

phoneext={'david':1410,'brad':1137}
keys = (phoneext.keys())

#dict_keys(['brad', 'david'])
print(list(phoneext.keys()))
#['brad', 'david']
print(phoneext.values())
#dict_values([1137, 1410])
print(list(phoneext.values()))
#[1137, 1410]
print(phoneext.items())
#dict_items([('brad', 1137), ('david', 1410)])
print(list(phoneext.items()))
#[('brad', 1137), ('david', 1410)]
print(phoneext.get("kent","NO ENTRY"))
#'NO ENTRY'

counter = 1 
while counter <=5: 
	print("Hello!")
	counter += 1

for item in [1,2,3,4]:
	print(item)

import math
n = 10
if n<0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))

score  = 85
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')

if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')




