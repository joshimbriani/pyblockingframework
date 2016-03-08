class EntityProfile:

	attributes = {}
	url = ""

	def __init__(self):
		self.attributes = {}
		self.url = ""

	def addAttribute(self, attributeName, attributeValue):
		self.attributes[attributeName] = attributeValue

	def getAttributes(self):
		return self.attributes

	def getUrl(self):
		return self.url
