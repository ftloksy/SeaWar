from carObj import carObj
from landMineCreater import landMineCreater
import pygame, os, sys
from globalObj import globalObj
from playerObj import playerObj
from focusObj import focusObj
from pygame import *
from random import randint


class gamePlay(object):
	
	def __init__(self):
		pygame.init()
		
	def load_fileObj(self):
		self.si = globalObj()
		
	def _set_fonts(self):
		self.big_font = self.si.load_font(96)
		self.font = self.si.load_font(24)
		self.menu_font = self.si.load_font(18)
		self.small_font = self.si.load_font(12)		
		
	def play_music(self, filename):
		if pygame.mixer:
			pygame.mixer.music.fadeout(1000)
			music = os.path.join(self.si.dir, filename)
			pygame.mixer.music.load(music)
			pygame.mixer.music.play(-1)

	def set_car(self):
		self.cars_xy = [(100, 100), (500, 280)]
		for i in range(0, len(self.cars_xy)):
			car = carObj(self.si, i, (self.cars_xy[i][0], self.cars_xy[i][1]))
			self.si.carsprites.add(car)

# Move focus to player obj.

	def _set_joystick_players(self, i):
			j = joystick.Joystick(i)
			j.init()
			focus = focusObj(self.si, i, self.focus_start_location[i], j)
			player = playerObj(self.si, i, focus, self.player_location[i])
			self.si.focussprites.add(focus)
			self.si.playersprites.add(player)
	
	def _set_nonjoystick_players(self, i):
			focus = focusObj(self.si, i, self.focus_start_location[i])
			player = playerObj(self.si, i, focus, self.player_location[i])
			self.si.playersprites.add(player)
			if self.si.joystick_n == 0 and self.si.keyboard_h and i == 0:
				self.si.focussprites.add(focus)
			
	def _set_players(self):
		# you can add more, when you have more than two joystick.
		self.player_location = [(0,10), (200, 10)] 
		self.focus_start_location = [(500, 100), (100, 280)]

		# If computer have more then two joystick, then the program will has bug.
		if self.si.joystick_n >= 2: # Has two player
			for i in range(0, self.si.joystick_n):
				self._set_joystick_players(i)
		if self.si.joystick_n == 1: # Just one player.
			for i in range(0, 2):
				if i == 0:
					self._set_joystick_players(i)
				if i == 1:
					self._set_nonjoystick_players(i)
		if self.si.joystick_n == 0:
			for i in range(0, 2):
				self._set_nonjoystick_players(i)
	
	def set_landMineCreater(self):
		self.lmc = landMineCreater(self.si)
		
	def _base_event_handle(self, state=None):
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					sys.exit()
				elif e.key == K_h:
					self._show_help()
				elif e.key == K_SPACE:
					return 1
				elif e.key == K_k:
					self.si.keyboard_h = 1;
					return 1
				elif e.key == K_s:
					self._screen_save()
		
	def readyGame(self):
			self.si.bg.screen.blit(self.si.bg.background, (0, 0))
			self._display_infomation_bar(0)
			self.si.bg.screen.blit(
				self.big_font.render('Sea War', 1, (100,100,100)), (40,10))
			self.si.bg.screen.blit(
				self.font.render('Milker\'s Solo Entry for pyweek 6 ', 1, 
					(100,100,100)), (40,100))
			self.si.bg.screen.blit(
				self.small_font.render('Copyright (c) by http://www.milk2cows.com ', 1, 
					(100,100,100)), (40,140))	
			self.si.bg.screen.blit(
				self.small_font.render('2008-4 ', 1, 
					(100,100,100)), (40,160))
			if self.si.joystick_n > 0:
				self.si.bg.screen.blit(
					self.menu_font.render('PRESS [SPACEBAR] TO PLAY IN JOYSTICK MODE', 1, 
						(0,128,0)), (40,330))
			self.si.bg.screen.blit(
				self.menu_font.render('PRESS [h] TO HELP', 1, 
					(0,128,0)), (40,360))	
			self.si.bg.screen.blit(
				self.menu_font.render('PRESS [ESC] TO QUIT', 1, 
					(0,128,0)), (40,390))
			if self.si.joystick_n == 0:
				self.si.bg.screen.blit(
					self.menu_font.render('PRESS [k] TO PLAY IN KEYBOARD MODE', 1, 
						(0,128,0)), (40,420))
				self.si.bg.screen.blit(
					self.small_font.render('KEYBOARD MODE IS SINGLE USER MODE', 1, 
						(0,128,0)), (40,440))
					
		
#			self.si.bg.screen.blit(self.si.introimage.convert_alpha(), (0,0))
			display.flip()
			pygame.mixer.music.set_volume(0.8)
			while True:
				if self._base_event_handle(): return


	def _show_help(self):
		self.si.bg.screen.blit(self.si.bg.background, (0, 0))
		if self.si.keyboard_h and not self.si.joystick_n:
			self.si.bg.screen.blit(self.si.keyimage.convert_alpha(), (100,20))
		else:
			self.si.bg.screen.blit(self.si.helpimage.convert_alpha(), (100,50))
			
		self._display_infomation_bar(0)
		display.flip()
		
		pygame.mixer.music.set_volume(0.8)
		
		while True:
			if self._base_event_handle(): return
						
	def _screen_save(self):
		pygame.image.save(self.si.bg.screen, '/tmp/save.bmp')

	def run(self):
		pygame.mixer.music.set_volume(0.2)
		clock = pygame.time.Clock()
		# I accept this speed. maybe it can change use the 
		clock.tick(10)
		
		while True:
			if self.si.keyboard_h:
				clock.tick(10)
			self._base_event_handle('run')
			pygame.mixer.music.set_volume(0.2)
			self.lmc.bcreate()

			self.si.boomsprites.update()
			self.si.carsprites.update()
			self.si.landMinesprites.update()
			self.si.firesprites.update()

			# If the computer have two joystick, it will has bug.
#			for i in range(0, self.si.joystick_n):
#				self.si.catchsprites[i].update()
#				self.si.marksprites[i].update()

#	change it to handle the keyboard bug.
			for i in range(0, 2):
				self.si.catchsprites[i].update()
				self.si.marksprites[i].update()
			
			self.si.focussprites.update()

			if self.si.count_total_cars_power():
				self.alive = 1
			else:
				self.alive = 0
			self.si.playersprites.update()
			if self.alive:
				self._alive()
			else:
				self._gameover()
	
	def _alive(self):
		self._display_anything()
	
	def _gameover(self):
		self.gameover_font = self.si.load_font(48)
		while True:
			if self._base_event_handle(): return
			self.si.bg.screen.blit(
				self.gameover_font.render('GameOver', 1, (128, 0, 0)), (10,320))
			self._display_infomation_bar()
			display.flip()

	def _tmp_spriteGroup_draw(self, sg):
		tmp = sprite.Group()
		for m in sg.sprites():
			tmp.add(m)
			tmp.draw(self.si.bg.screen)
			
	def _display_anything(self):
		self.si.bg.screen.blit(self.si.bg.background, (0, 0))
		self.si.bg.screen.blit(self.si.dimage.convert_alpha(), (0,0))
		
		self.si.landMinesprites.draw(self.si.bg.screen)
		self._addon_draw(self.si.landMinesprites)
		self.si.carsprites.draw(self.si.bg.screen)
		self._addon_draw(self.si.carsprites)
		self.si.firesprites.draw(self.si.bg.screen)

#	change it to handle the keyboard bug.
		for i in range(0, 2):
			self._tmp_spriteGroup_draw(self.si.marksprites[i])
			self._tmp_spriteGroup_draw(self.si.catchsprites[i])
			self._addon_draw(self.si.catchsprites[i])
		
		self.si.focussprites.draw(self.si.bg.screen)
		
		self._display_infomation_bar()

		display.flip()
		
	def _display_infomation_bar(self, state=1):
		# handle the bottom infomation bar.
		self.si.bg.screen.blit(self.si.bg.bbar, (0, 380))
		if state == 1:
			self.si.playersprites.draw(self.si.bg.bbar)

# Display the game_logo image.
		self.si.bg.screen.blit(
			self.si.logoimage, (400,390))

	def _addon_draw(self, sp):
		for l in sp.sprites():
			if l.power > 30:
				draw.circle(self.si.bg.screen, 
					(255, 255, 255), 
					l.center, int(l.power/10), 3)
			
			self._draw_line(l, 5, l.power)
			self._draw_line(l, 10, l.high_point)
			self._draw_line(l, 15, l.life)

	def _draw_line(self, l, ny, info):
		draw.line(self.si.bg.screen, (255, 255, 255), 
			(l.rect.left, l.rect.top - ny), (l.rect.left + info / 5, l.rect.top - ny), 3)

	def main(self):
		
		while True:
			self.load_fileObj()
			self._set_fonts()

			self.play_music('ballada.ogg')	

			self.readyGame()
			self._set_players()
			self.set_landMineCreater()
			
			self.set_car()
			self.run()
			
if __name__ == "__main__":
	g = gamePlay()
	g.main()