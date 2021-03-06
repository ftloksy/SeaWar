# This is the simple Image handler for cat and mouse game.

from pygame import *
from random import randint
from turnImgObj import turnImgObj
import os

class carObj(turnImgObj):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, si, id, center):
		self.type = 'car'
		self.power = 150
		self.high_point = 0
		self.id = id
		self.turn_speed = 0.3
		turnImgObj.__init__(self, si, center)

	def update(self):
		self._objs_update_before()

		# car create a car, when car has full power!!
		if self.power > 200:
			car = carObj(self.si, self.id, self.center)
			car.power = 100
			self.add_cars(car)
			self.power = (self.power/2) - 50
		self._random_walk()
		self._dont_walk_out_screen()
		self._objs_update_after()

	def add_cars(self, car):
		self.si.carsprites.add(car)
		self.si.thud_sound.play()
	
	def _random_walk(self):
		self.move(randint(-5,5),randint(-5,5))

	def _check_hit_myselfs(self):
		if not self.si.catchsprites[self.id].has(self):
			tmp = self.cars.copy()
			tmp.remove(self)
			for c in sprite.spritecollide(self, tmp, 0):
				if not c.id == self.id or self.power > 155:
					self.hit()
					c.hit()
					self.si.yeow_sound.play()
					self.power -= ( (c.power/3) * 2)
					c.power -= ( (c.power/3) * 2 )
					if c.power < 50:
						self.power += ( c.power * 2 )
						c.boom()
					if self.power < 50:
						self.boom()
