from rdflib import *
import csv
import urlparse
from collections import *
import numpy

#======================================map reduce adaptation of the infix extraction ====================================================#
# map phase
# Read rdf data file and ouput (key, value) pair for each URI (domain, whole URI)

def totalDescription(data1, data2):

	g = ConjunctiveGraph()
	g2 = ConjunctiveGraph()
	g3 = ConjunctiveGraph()

	data1 = g.parse("http://source.data.gov.uk/data/education/bis-research-explorer/2010-03-04/education.data.gov.uk.nt", format='nt')
	data2 = g2.parse("http://source.data.gov.uk/data/research/bis-research-explorer/2010-03-04/research-schema.rdf")
	#data3 = g3.parse ("http://live.dbpedia.org/data/Python_(programming_language).ntriples", format = 'nt')
	data1_list = []
	data2_list = []

	for s,p,o in g: # read in subject, predicate, and objects in URIs in data1
		s = s.encode('utf-8')
		p = p.encode('utf-8')
		o = o.encode('utf-8')

		s_split = urlparse.urlsplit(s).path
		p_split = urlparse.urlsplit(p).path
		o_split = urlparse.urlsplit(o).path
		s_dash = s_split.split('/')
		p_dash = p_split.split('/')
		o_dash = o_split.split('/')
		entity = s_dash + p_dash + o_dash
		data1_list.append(entity)

	for s,p,o in g2: # read in subject, predicate, and objects in URIs in data 2
		s = s.encode('utf-8')
		p = p.encode('utf-8')
		o = o.encode('utf-8')
		s_split = urlparse.urlsplit(s).path
		p_split = urlparse.urlsplit(p).path
		o_split = urlparse.urlsplit(o).path
		s_dash = s_split.split('/')
		p_dash = p_split.split('/')
		o_dash = o_split.split('/')
		entity = s_dash + p_dash + o_dash
		data2_list.append(entity)

	blocks = {}

	# ========================================== Generate Blocks ==================================================================#
	for dataItem in data1_list + data2_list:
		for dataAttribute in dataItem:
			#print dataAttribute
			wordList = dataAttribute.split(' ')
			#print wordList

			for word in wordList:
				if word in blocks and word != '':
					blocks[word].append(dataItem)
				elif word not in blocks and word != '':
					blocks[word] = []
					blocks[word].append(dataItem)

	print "=============================  Finished ======================================================================================="
	print "Number of blocks", len(blocks)
	item_num_list = []
	for i in xrange(len(blocks)):
		temp = blocks.values()[i]
		item_num = len(temp)
		item_num_list.append(item_num)
	print "Average number of items in block:", numpy.mean(item_num_list)

	return blocks
