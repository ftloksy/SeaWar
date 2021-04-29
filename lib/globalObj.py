import os, pygame
from pygame.locals import *
from pygame import *
from bgHandle import bgHandle

class globalObj(object):
	def __init__(self):
		if not pygame.font: 
			print 'Warning, fonts disabled'
		if not pygame.mixer: 
			print 'Warning, sound disabled'
		self.dir = "data"
		self.set_background()

		self.background_image()
		self.roadbox_image_list()
		self.boom_image_list()
		self.fire_image_list()
		self.car_img_lists()
		self.mark_img_lists()
		self.focus_img_lists()
		self.people_image_list()
		self.load_thud_sound()
		self.load_yeow_sound()
		self.load_introimage_image()
		self.load_helpimage_image()
		self.load_hitimage_image()
		self.set_boomsprites()
		self.set_landMinesprites()
		self.set_carsprites()
		self.set_labelsprites()
		self.set_firesprites()
		self.set_playersprites()
		self.set_focussprites()
		self.set_marksprites()
		self.set_catchsprites()
		self.load_fire_sound()
		self.load_logo_image()
		self.load_player_image()
		self.count_joystick_n()
		
		# Keyboard handle
		self.keyboard_h = 0
		self.load_keyboardimage_image()

	def load_image(self, name, colorkey=None):
		fullname = os.path.join(self.dir, name)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image:', fullname
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image

	def load_sound(self, name):
		class NoneSound:
			def play(self): pass
		if not pygame.mixer or not pygame.mixer.get_init():
			return NoneSound()
		fullname = os.path.join(self.dir, name)
		try:
			sound = pygame.mixer.Sound(fullname)
		except pygame.error, message:
			print 'Cannot load sound:', fullname
			raise SystemExit, message
		return sound
	
	def load_font(self, size, name="airstrip.ttf"):
		fullname = os.path.join(self.dir, name)
		self.font_file_obj = open(fullname, 'rb')
		pygame.font.init()
		font = pygame.font.Font(self.font_file_obj, size)
		return font
	
	def image_list(self, list):
		self.imagelist = []
		for i in list:
			image = self.load_image(i, -1)
			self.imagelist.append(image)
			
	def load_image_list(self, img_list):
		img_obj_list = []
		for i in img_list:
			image = self.load_image(i,-1)
			img_obj_list.append(image)
		return img_obj_list
			
#######################################
	
	def background_image(self, filename="bg-640-380-new.png"):
		self.dimage = self.load_image(filename, -1)
		self.dimage_rect = self.dimage.get_rect() 
			
	def roadbox_image_list(self, rbox_obj_img_list = ['sea_nettle1.png', 'sea_nettle2.png',
				'sea_nettle3.png', 'sea_nettle4.png']):
		self.rbox_obj_img_list = rbox_obj_img_list
		self.rbox_image_list = self.load_image_list(self.rbox_obj_img_list)

	def boom_image_list(self, boom_obj_img_list =  ['bubble1.png', 
		'bubble2.png', 'bubble3.png', 'bubble4.png']):	
		self.boom_obj_img_list = boom_obj_img_list
		self.boom_image_list = self.load_image_list(self.boom_obj_img_list)
		
	def people_image_list(self, people_obj_img_list =  ['people1.png', 
		'people2.png', 'people3.png']):	
		self.people_obj_img_list = people_obj_img_list
		self.people_image_list = self.load_image_list(self.people_obj_img_list)
		
	def fire_image_list(self, fire_obj_img_list = ['fire1.png', 
		'fire2.png', 'fire3.png']):
		self.fire_obj_img_list = fire_obj_img_list
		self.fire_image_list = self.load_image_list(self.fire_obj_img_list)
		
	def car_img_lists(self, cars_imglist =  [['boctopus1.png', 'boctopus2.png', 
				'boctopus3.png', 'boctopus4.png'],
				['yoctopus1.png', 'yoctopus2.png', 
				'yoctopus3.png', 'yoctopus4.png']]):

		self.cars_imglist = cars_imglist
		self.car_image_list = []
		for i in self.cars_imglist:
			self.car_image_list.append( self.load_image_list(i) )

	def focus_img_lists(self, focus_imglist = [['bfocus1.png', 'bfocus2.png'],
				['gfocus1.png', 'gfocus2.png']]):

		self.focus_imglist = focus_imglist
		self.focus_image_list = []
		for i in self.focus_imglist:
			self.focus_image_list.append( self.load_image_list(i) )

	def mark_img_lists(self, marks_imglist = [['bmark1.png', 
			'bmark2.png', 'bmark3.png'],
			['gmark1.png', 'gmark2.png', 'gmark3.png']]):

		self.marks_imglist = marks_imglist
		self.mark_image_list = []
		for i in self.marks_imglist:
			self.mark_image_list.append( self.load_image_list(i) )


		
	def load_player_image(self):
		self.player_image = self.load_image('player.png', -1)
	
	def load_thud_sound(self):
		self.thud_sound = self.load_sound('46261__PhreaKsAccount__Coachgun_Fire1.wav')

	def load_yeow_sound(self):
		self.yeow_sound = self.load_sound('44429__thecheeseman__hurt2.wav')
		
	def load_introimage_image(self):
		self.introimage = self.load_image('sea_war_logo.png', -1)
		
	def load_helpimage_image(self):
		self.helpimage = self.load_image('gamepad.png', -1)
	
	def load_keyboardimage_image(self):
		self.keyimage = self.load_image('keyboard-control.png', -1)
		
	def load_hitimage_image(self):
		self.hitimage = self.load_image("x.png", -1)
	
	def load_logo_image(self):
		self.logoimage = self.load_image("sea_war_logo3.png")
		
	def set_boomsprites(self):
		self.boomsprites = sprite.Group()
		
	def load_fire_sound(self):
		self.fire_sound = self.load_sound('fire.ogg')
		
	def set_landMinesprites(self):
		self.landMinesprites = sprite.Group()
		
	def set_carsprites(self):
		self.carsprites = sprite.Group()
		
	def set_labelsprites(self):
		self.labelsprites = sprite.Group()
	
	def set_firesprites(self):
		self.firesprites = sprite.Group()
		
	def set_playersprites(self):
		self.playersprites = sprite.Group()
		
	def set_focussprites(self):
		self.focussprites = sprite.Group()
	
	def set_marksprites(self):
		self.marksprites = [sprite.GroupSingle(), sprite.GroupSingle()]
	
	def set_catchsprites(self):
		self.catchsprites = [sprite.GroupSingle(), sprite.GroupSingle()]

	def set_background(self): 
	
		# set the background.
		self.bg = bgHandle()
		self.bg.set_background()
		self.bg.set_bottom_bar()
		self.bgarea = Rect(0, 0, 640, 380)

# If more then two joystick, has bug in here.		
	def count_total_cars_power(self):
		self.ctotal = [0, 0]
		self.carn = [0, 0]
		for c in self.carsprites.sprites():
			if c.id == 0:
				self.ctotal[0] += c.power
				self.carn[0] += 1
			if c.id == 1:
				self.ctotal[1] += c.power
				self.carn[1] += 1
		for i in range(0, 2):
			for c in self.catchsprites[i].sprites():
				if c.type == 'car':
					if c.id == 0:
						self.ctotal[0] += c.power
						self.carn[0] += 1
					if c.id == 1:
						self.ctotal[1] += c.power
						self.carn[1] += 1
		if self.carn[0] == 0 or \
			self.carn[1] == 0:
				return 0 # GAMEOVE
		else:
			return 1 # alive.
		
	def count_joystick_n(self):
		self.joystick_n = joystick.get_count()