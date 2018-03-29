f = open('x.txt','r+')

listoflines = f.readlines()

length = len(listoflines) - 1

datelist, monthlist, openplist, closeplist = zip(*[ (listoflines[i].split()[0],  listoflines[i].split()[1], int(listoflines[i].split()[2]), int(listoflines[i].split()[3]) ) for i in range(1,length)])

print(datelist,monthlist,openplist, closeplist)

print(sum(openplist)/7 , sum(closeplist)/7)   

string = str(sum(openplist)/7) + ' ' + str(sum(closeplist)/7) + '\n'

f.write(string)

f.close()
