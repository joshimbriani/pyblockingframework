from entityProfile import EntityProfile

class Block:

	entityProfiles = []

	def __init__(self):
		entityProfiles = []

	def addEntityProfile(self, entityProfile):
		entityProfiles.append(entityProfile)

	def calculateComparisons(self):
		return len(entityProfiles)**2

	def calculateMatching(self):
		#Will return a tuple containing the number of matching records and the total records in the block
		return (2, 6)
