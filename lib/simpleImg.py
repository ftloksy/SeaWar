# This is the simple Image handler for cat and mouse game.

from pygame import *
from random import randint
import os

class simpleImg(sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, si, speed=5):
		sprite.Sprite.__init__(self) #call Sprite initializer
		self.speed = speed
		self.si = si
		self.booms = si.boomsprites
		self.lms = si.landMinesprites
		self.cars = si.carsprites
		self.focuss = si.focussprites
		self.now_img = 0
		self.turnImg()
		self.state_x = self.state_y = 0
		self.hit_image = self.si.hitimage
		
	def move(self, x, y):
		self.rect = self.rect.move(x, y)
	
	def hit(self):
		self.image = self.hit_image
		self.rect = self.image.get_rect(center = self.center)
		
	def turnImg(self, turnspeed = 0.3):
		if self.type == 'landmine':
			if self.now_img >= len(self.si.rbox_image_list):
				self.now_img = 0
			self.image = self.si.rbox_image_list[int(self.now_img)]
		elif self.type == 'car':
			if self.now_img >= len(self.si.car_image_list[self.id]):
				self.now_img = 0
			self.image = self.si.car_image_list[self.id][int(self.now_img)]
		elif self.type == 'mark':
			if self.now_img >= len(self.si.mark_image_list[self.id]):
				self.now_img = 0
			self.image = self.si.mark_image_list[self.id][int(self.now_img)]
		elif self.type == 'fire':
			if self.now_img >= len(self.si.fire_image_list):
				self.now_img = 0
			self.image = self.si.fire_image_list[int(self.now_img)]
		elif self.type == 'focus':
			if self.now_img >= len(self.si.focus_image_list):
				self.now_img = 0
			self.image = self.si.focus_image_list[self.id][int(self.now_img)]			

		self.now_img += turnspeed
		self.rect = self.image.get_rect(center = self.center)
		
	def boom(self):
		try:
			self.si.firesprites.remove(self.fire)
			self.fire.kill()
		except AttributeError:
			pass
		self.kill()
		
	def _dont_walk_out_screen(self):
		if self.rect.left < self.si.bgarea.left:
			self.rect.right = self.si.bgarea.right
		if self.rect.right > self.si.bgarea.right:
			self.rect.left = self.si.bgarea.left
		if self.rect.top < self.si.bgarea.top:
			# have bug in here.
			self.rect.bottom = self.si.bgarea.bottom
		if self.rect.bottom > self.si.bgarea.bottom:
			self.rect.top = self.si.bgarea.top
			
