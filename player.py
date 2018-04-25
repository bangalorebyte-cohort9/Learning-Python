#!/usr/bin/env python3

class Player:

	numPlayer = 0
	
	def __init__(self,firstname,lastname,nplayer,weight,height):
		self.firstname = firstname
		self.lastname = lastname
		self.nPlayer = nplayer
		self.weight = weight
		self.height = height
		self.profilefilehandler = None
		self.profiledata = None
		self.profilefilename = None
		Player.numPlayer = Player.numPlayer+1

	def setprofilefilename(self,filename):
		self.profilefilename = filename

	def kick(self):
		self.ball.running()

	def getfirstname(self):
		return self.firstname

	def setfirstname(self,firstname):
		self.firstname = firstname

	def __str__(self):
		return "%s , %s" %(self.firstname, self.lastname)

	def __repr__(self):
		return "Player(%s,%s)" %(self.firstname,self.lastname)

	def __add__(self,player):
		return self.nPlayer + player.nPlayer

	def __enter__(self):

		if self.profilefilehandler is not None:
			raise RuntimeError('File already opened')

		self.profilefilehandler = open(self.profilefilename,'r')
		return self.profilefilehandler

	def __exit__(self,exc_ty, exc_val, tb):
		self.profilefilehandler.close()
		self.profilefilehandler = None

	@classmethod
	def getnumplayers(cls):
		print('No. of players so far are :', cls.numPlayer)
		return(cls.numPlayer)

	@staticmethod
	def bmi(weight, height):
		return (weight / (height*height))


class CricketPlayer(Player):

	def __init__(self,role,fn,ln,np,weight,height):
		super().__init__(fn,ln,np,weight,height)
		self.role = role

	def setrole(self,role):
		self.role = role

	def getrole(self,role):
		return self.role



if __name__ == '__main__':

	p1 = Player('Virat','Kohli',1,50,5)
	p2 = Player('Sachin','Tendulkar',2,57,5.5)
	p3 = Player('Kapil','Dev',3,58,5)
	bmi = Player.bmi(p1.weight,p1.height)
	
	print(bmi)
	print('No of players created ', Player.numPlayer)

	p1.setprofilefilename('Virat.txt')
	# Using context manager with Player class

	with p1 as f:
		p1.profiledata = f.read()

	print(p1.profiledata)
	#with p1 as f:
	#	p1.profiledata = f.read()

	# Inherited class calls

	c1 = CricketPlayer('Batsman',p1.firstname,p1.lastname,p1.nPlayer,p1.weight,p1.height)
	print(c1.firstname)

	print(CricketPlayer.bmi(c1.weight,c1.height))
	print(c1.getfirstname())
	print(CricketPlayer.numPlayer)




	
	




