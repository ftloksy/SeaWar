# This is the Road Obj.

from childObj import childObj
		
class fireObj(childObj):
	def __init__(self, si, center, parent):
		childObj.__init__(self, si, center, 'fire', parent)
	
	def update(self):
		self._update_before()
		if not self.si.carsprites.has(self.parent) and \
			not self.si.landMinesprites.has(self.parent):
				self.kill()
				