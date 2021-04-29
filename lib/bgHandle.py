from pygame import *
import os

class bgHandle(object):
	def __init__(self):
#		self.size = width, height = 800, 600
		self.size = width, height = 640, 480
		self.screen = display.set_mode(self.size)
		display.set_caption('Sea War')
#		display.toggle_fullscreen()

	def set_background(self):
		#Create The Backgound
		self.background = self._set_bg(self.screen.get_size(), (128,0,0))
	
	def _set_bg(self, size, color):
		sf = Surface(size).convert()
		sf.fill(color)
		return sf
	
	def set_bottom_bar(self):
		self.bbar = self._set_bg((640,100),(128,0,0))
