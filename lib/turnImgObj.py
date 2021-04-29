from simpleImg import simpleImg
from pygame import *
from fireObj import fireObj
import os

class turnImgObj (simpleImg):
	def __init__(self, si, center, parent=None):
		self.center = center
		self.life = 1000
		simpleImg.__init__(self, si)
		self.fire = fireObj(si, center, self)
		self.si.firesprites.add(self.fire)
		self.rect = self.image.get_rect()
		self.rect.center = self.center
	
	def _has_fire(self):
		if self.si.firesprites.has(self.fire):
			if self.power > 75: 
				self.si.firesprites.remove(self.fire)
		else:
			if self.si.boomsprites.has(self) or \
				self.si.landMinesprites.has(self) or \
				self.si.carsprites.has(self) :
				if self.power < 75:
					self.si.firesprites.add(self.fire)
	
	def _update_high_power(self):
		if self.power > self.high_point:
			self.high_point = self.power
			
	def _objs_update_before(self):
		self.life -= 1
		if self.life < 0:
			self.boom()
		if self.power < 0:
			self.boom()
		self.center = self.rect.center
		self.turnImg(turnspeed = self.turn_speed)
		
	def _objs_update_after(self):
		self._check_hit_myselfs()
		self._has_fire()
		self._update_high_power()