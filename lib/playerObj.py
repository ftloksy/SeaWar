#This is the Obj for Player.

import sys
from pygame import *
from markObj import markObj
import pygame
from pygame.locals import *

class playerObj(sprite.Sprite):
	def __init__(self, si, id, focus, topleft):
		sprite.Sprite.__init__(self) #call Sprite initializer
		self.si = si
		self.id = id
		self.font = self.si.load_font(24)
		self.small_font = self.si.load_font(12)
		self.image = Surface((200,100)).convert()
		self.image.fill((128,0,0))
		self.now_img = 0
		self.now_img_people = 0
		self.focus = focus
		self.item_on_hold = 0
		self.item_on_take = 0
		
		self.info_item = sprite.GroupSingle()
		self.info_take = sprite.GroupSingle()
		self.rect = self.image.get_rect(topleft=topleft)
	
	def update(self):
		self._set_focus_hit_rect()
		self._display_team_info()
		if (self.id == 0 and self.si.keyboard_h) or self.focus.joystick:
				self._display_two_icon()
				self._scan_object_info()
				self._take_object_info()
				self._display_item_info()
				self._if_die_empty_take()
				self._display_take_info()
				self._mark_and_release_item()
				self._take_and_relese_item()
		else:
			pass
	
	def _if_die_empty_take(self):
		if len(self.info_take.sprites()) == 0:
			self.item_on_take = 0
	
	def _mark_item(self):
		for it in self.info_item.sprites():
			m = markObj(self.si, self.id, it.center, it)
			self.si.marksprites[self.id].add(m)
		self.item_on_hold = 1
	
	def _release_mark_item(self):
		self.si.marksprites[self.id].empty()
		self.item_on_hold = 0
	
	def _mark_and_release_item_handler(self, mark, release_m):
		if mark:
			self._mark_item()
		elif release_m:
			self._release_mark_item()
		elif 	len(self.si.marksprites[self.id].sprites()) == 0:
			self.item_on_hold = 0		
					
	def _mark_and_release_item(self):
		# Mark the Object and Ready Display it in player area, 
		# see self._display_item_info()
		if (self.id == 0 and self.si.keyboard_h) or self.focus.joystick:
			if self.focus.joystick:
				self._mark_and_release_item_handler(
					self.focus.joystick.get_button(4),
					self.focus.joystick.get_button(6) )
					
			# Use keyboard to handle samething.
			elif self.id == 0 and self.si.keyboard_h:
				self.key = pygame.key.get_pressed()
				self._mark_and_release_item_handler(
					self.key[K_f], self.key[K_v])
					
	def _take_item(self):
		for it in self.info_take.sprites():
			self.si.catchsprites[self.id].add(it)
			self.focus.set_move_item(it)
			if self.si.carsprites.has(it):
				self.si.carsprites.remove(it)
			elif self.si.landMinesprites.has(it):
				self.si.landMinesprites.remove(it)
		self.item_on_take = 1
	
	def _release_take_item(self):
		for it in self.info_take.sprites():
			self.si.catchsprites[self.id].remove(it)
			if it.type == 'car':
				self.si.carsprites.add(it)
			elif it.type == 'landmine':
				self.si.landMinesprites.add(it)
			it.rect.center = self.focus.rect.center
		self.item_on_take = 0
		self.focus.set_release_catched()
		
	def _take_and_release_item_handler(self, take, release_t):
		if take:
			self._take_item()
		elif release_t:
			self._release_take_item()
					
	def _take_and_relese_item(self):
		if (self.id == 0 and self.si.keyboard_h) or self.focus.joystick:
			if self.focus.joystick:
				self._take_and_release_item_handler(
					self.focus.joystick.get_button(5),
					self.focus.joystick.get_button(7))

			elif self.id == 0 and self.si.keyboard_h:
				self.key = pygame.key.get_pressed()
				self._take_and_release_item_handler(
					self.key[K_g], self.key[K_b])		

	def _object_info(self, v, sg):
		if not v:
			for m in self.si.landMinesprites.sprites():
				if self.focus_hit_rect.colliderect(m.rect):
					sg.add(m)
			for c in self.si.carsprites.sprites():
				if self.focus_hit_rect.colliderect(c.rect):
					sg.add(c)

	def _scan_object_info(self):
		# first scan the landMine and then cars.
		# Just keep one on the sprite.Goup.
		# ToDo: keep display info of myself first.

		self._object_info(self.item_on_hold, self.info_item)
		
	def _take_object_info(self):
		self._object_info(self.item_on_take, self.info_take)
		
	def _set_focus_hit_rect(self):
		self.focus_hit_rect = self.focus.rect.inflate(-20,-20)
		
	def _display_object_info(self, sg, v):
		for i in sg.sprites():
			self.image.blit(transform.scale(i.image, (40,40)), (v, 10))
			self.image.blit(
				self.small_font.render(
					'p:%s' %i.power, 1, (255, 255, 255)),
				(v,50))
			self.image.blit(
				self.small_font.render(
					'h:%s' %i.high_point, 1, (255, 255, 255)),
				(v,60))
			self.image.blit(
				self.small_font.render(
					'l: %s' %i.life, 1, (255, 255, 255)),
				(v,70))		
	
	def _display_item_info(self):
		self._display_object_info(self.info_item, 100)

	def _display_take_info(self):
		self._display_object_info(self.info_take, 150)
	
	def _display_two_icon(self):
		self.image.blit(
			transform.scale(self.si.focus_image_list[self.id][0], (20, 20))
			, (170, 0))
		self.image.blit(
			transform.scale(self.si.mark_image_list[self.id][0], (20, 20))
			, (130,0))

	def _display_team_info(self):
		self.image.blit(self.si.player_image, (0,0))
		if self.now_img >= len(self.si.car_image_list):
				self.now_img = 0	
		if self.now_img_people >= len(self.si.people_image_list):
				self.now_img_people = 0
				
		self.image.blit(
			transform.scale(self.si.car_image_list[self.id][int(self.now_img)], (30,30))
			, (5,10))
		self.image.blit(
			self.si.people_image_list[int(self.now_img_people)], (5, 45))
		
		self.now_img += 0.01	
		self.now_img_people += 0.05
		
		if self.si.ctotal[self.id] == 0:
			self.image.blit(
				self.font.render('LOST', 1, (100,100,100)), (40,10))
		else:
			self.image.blit(
				self.font.render('%s' %self.si.ctotal[self.id], 1, (100, 100, 100)), (40,10))
			self.image.blit(
				self.font.render('%s' %self.si.carn[self.id], 1, (100, 100, 100)), (40,40))
		
		# Display Computer: If it hasn't joystick
		if not ( self.id == 0 and self.si.keyboard_h ) and not self.focus.joystick:
				self.image.blit(
					self.font.render('Computer', 1, (0, 0, 128)), (75,35))
