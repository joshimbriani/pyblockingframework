from __future__ import division
from totalDescription import totalDescription
from BSL import BSL
from blockingTokens import blockingTokens
from fuzzywuzzy import fuzz

class Comparer:

	data1 = []
	data2 = []
	comparisonMethod = ""

	def __init__(self, data1, data2, comparisonMethod):
		self.data1 = data1
		self.data2 = data2
		comparisonMethod = comparisonMethod

	def runTotalDescription(self):
		self.temp = totalDescription(self.data1, self.data2)
		self.blocks = blockingTokens(self.data1, self.data2)
		#print blocks

	def runBlockingTokens(self):
		self.blocks = blockingTokens(self.data1, self.data2)
		#print blocks

	def runBSL(self, data1, data2):
		self.blocks = BSL(data1, data2)
		#print blocks

	def evaluate(self, blocks, lenData1, lenData2):
		totalComparisons = 0
		for block in self.blocks:
			if len(self.blocks[block]) == 0:
				totalComparisons += 0
			elif len(self.blocks[block]) == 1:
				totalComparisons += 0
			totalComparisons += (((len(self.blocks[block])-1)**2 + (len(self.blocks[block])-1)) / 2)
		#print totalComparisons, lenData1, lenData2
		RR = totalComparisons / (lenData1*lenData2)

		for block in self.blocks:
			for index, item in self.blocks[block].enumerate():
				for i in range(index, len(self.blocks[block]):
					fuzz.token_set_ratio(self.blocks[block][index][1], self.blocks[block][index][1])

		return RR
