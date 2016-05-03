from entityProfile import EntityProfile
from blocks import Block

def blockingTokens(data1, data2, mostImportant):

	blocks = {}

	for dataItem in data1 + data2:
		#for dataAttribute in dataItem:
		wordList = dataItem[mostImportant].split(' ')
		for word in wordList:
			if word in blocks:
				blocks[word].append(dataItem)
			else:
				blocks[word] = []
				blocks[word].append(dataItem)

	return blocks
