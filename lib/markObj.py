from childObj import childObj
		
class markObj(childObj):
	def __init__(self, si, id, center, parent):
		self.id = id
		childObj.__init__(self, si, center, 'mark', parent)
		
	def update(self):
		self._update_before()
		if not self.si.landMinesprites.has(self.parent) and \
			not self.si.carsprites.has(self.parent) :
				self.boom()