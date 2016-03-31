import urlparse

def totalDescription(data1, data2):
	#implementation of infix from URI in python

	#loop over file to extract strings between backslashes and store in list
	p = urlparse.urlsplit('http://dblp.13s.de/d2r/resource/publications/books/sp/wooldridgeV99/ThalmannN99').path
	#p = /d2r/resource/publications/books/sp/wooldridgeV99/ThalmannN99

	splitted = p.split('/')
	print splitted
	for i in splitted:
    		print i
