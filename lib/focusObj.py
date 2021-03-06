from simpleImg import simpleImg
from pygame.locals import *
import pygame
		
class focusObj(simpleImg):
	def __init__(self, si, id, center, joystick=None):
		self.type = "focus"
		self.si = si
		self.id = id
		self.center = center
		self.joystick = joystick
		self.turn_speed = 0.1
		self.catched = 0
		simpleImg.__init__(self, si)
		
	def update(self):
		self.center = self.rect.center
		self.turnImg(turnspeed = self.turn_speed)
		if (self.id == 0 and self.si.keyboard_h) or self.joystick:
			if self.joystick:
				self._joystick_walk()
			elif self.id == 0 and self.si.keyboard_h:
				self._keyboard_walk()
			
			self._dont_walk_out_screen()
			if self.catched:
				self.move_it.rect.center = self.rect.center
	
	def set_release_catched(self):
		self.catched = 0
		self.move_it = None
	
	def set_move_item(self, move_it):
		self.catched = 1
		self.move_it = move_it

	def _keyboard_walk(self):
		self.key = pygame.key.get_pressed()
		press_x = 0
		press_y = 0
		if self.key[K_w]:
			press_y = -1
		elif self.key[K_s]:
			press_y = 1
		elif self.key[K_a]:
			press_x = -1
		elif self.key[K_d]:
			press_x = 1
		else:
#			press_x = press_y = 0
			pass
		self._walk(press_x, press_y)

	def _joystick_walk(self):
		self._walk(self.joystick.get_axis(3), self.joystick.get_axis(4))
		
	def _walk(self, press_x, press_y):
		self.x_axis = press_x
		self.y_axis = press_y
		self.x = self.y = 0
		if self.state_x == 1:
			self.x = 1
		elif self.state_x == -1:
			self.x = -1
			
		if self.state_y == 1:
			self.y = 1
		elif self.state_y == -1:
			self.y = -1

		if (self.x_axis):
			self.x = int(self.x_axis * 2)
			self.state_x = self.x
			self.state_y = 0
		elif (self.y_axis):
			self.y = int(self.y_axis * 2)
			self.state_y = self.y
			self.state_x = 0
		else:
			pass
		
		self.x = self.speed * self.x
		self.y = self.speed * self.y
		self.move(self.x, self.y)