from entityProfile import EntityProfile
from blocks import Block

def blockingTokens(entityProfiles):

	blocks = {}

	for profile in entityProfiles:
		for attributeKey, attributeValue in profile.attributes.iteritems():
			wordList = attributeValue.split(' ')
			for word in wordList:
				if word in blocks:
					blocks[word].append(profile)
				else:
					blocks[word] = []
					blocks[word].append(profile)

	return blocks
