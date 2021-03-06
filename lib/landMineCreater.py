from landMine import landMine
from random import randint

class landMineCreater(object):
	def __init__(self, si):
		self.createtime = 0
		self.si = si
	
	def bcreate(self):
		self.createtime += 1
		if self.createtime > 5:
			# has bug in si.bgarea.bottom.
			center = (randint(0,self.si.bgarea.right), randint(0, self.si.bgarea.bottom))
			lm = landMine(self.si, center)
			self.add_landmine(lm)
			self.createtime = 0
	
	def add_landmine(self, lm):
		self.si.landMinesprites.add(lm)
		#self.si.thud_sound.play()