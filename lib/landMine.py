from turnImgObj import turnImgObj
from pygame import *

class landMine(turnImgObj):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, si, center):
		self.type = 'landmine'
		self.power = 0
		self.high_point = 0
		self.turn_speed = 0.1
		turnImgObj.__init__(self, si, center)
	
	def update(self):
		self._objs_update_before()
		self.power += 1

		# landMine have fix xy.
		if self.power > 300:
			self.hit_rect = self.rect.inflate(self.power/5, self.power/5)
		else: self.hit_rect = self.rect

		self.catched = 0
		for i in range(0, self.si.joystick_n):
			if self.si.catchsprites[i].has(self):
				self.catched = 1
				
		if not self.catched:
			self._check_hit_cars()
			self._objs_update_after()
		
	def _check_hit_myselfs(self):
		tmp = self.lms.copy()
		tmp.remove(self)
		hits = []
		for m in tmp.sprites():
			if self.hit_rect.colliderect(m):
				hits.append(m)
		for l in hits:
			self.hit()
			l.hit()
#			self.si.yeow_sound.play()
			self.power -= ( (l.power/3) * 2)
			l.power -= ( (l.power/3) * 2 )
			if l.power < 50:
				l.boom()
			if self.power < 50:
				self.boom()
				
	def _check_hit_cars(self):
		hits = []
		for c in self.cars.sprites():
			if self.hit_rect.colliderect(c):
				hits.append(c)
		for car in hits:
			car.hit()
			self.hit()
#			self.si.yeow_sound.play()
			self.power -= ( (self.power/3) * 2)
			car.power -= (self.power / 10)
			if self.power < 50:
				car.power += ( self.power * 5 )
				self.boom()
#			if car.power < 50:
#				car.boom()