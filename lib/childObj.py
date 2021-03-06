from simpleImg import simpleImg
		
class childObj(simpleImg):
	def __init__(self, si, center, type_name, parent):
		self.type = type_name
		self.si = si
		self.center = center
		self.parent = parent
		simpleImg.__init__(self, si)
		self.rect = self.image.get_rect()
		self.rect.center = center
	
	def update(self):
		self._update_before()

	def _update_before(self):
		self.turnImg()
		self.center = self.parent.rect.center