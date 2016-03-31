from totalDescription import totalDescription
from BSL import BSL

class Comparer:

	data1 = []
	data2 = []
	comparisonMethod = ""

	def __init__(self, data1, data2, comparisonMethod):
		self.data1 = data1
		self.data2 = data2
		comparisonMethod = comparisonMethod

	def runTotalDescription(self, data1, data2):
		blocks = totalDescription(data1, data2)
		print blocks

	def runBSL(self, data1, data2):
		blocks = BSL(data1, data2)
		print blocks

	def evaluate(self, blocks, lenData1, lenData2):
		totalComparisons = 0
		for block in blocks:
			totalComparisons += ((len(totalComparisons)**2 + len(totalComparisons)) / 2)
		RR = totalComparisons / (lenData1*lenData2)

		return RR
		
