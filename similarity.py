#!/usr/bin/python

def getJaccard( paragraph1, paragraph2):
	# get the union of the two lists

	wordList1 = set( paragraph1)
	wordList2 = set( paragraph2)

	intersection = list( wordList1 & wordList2)
	union = list( wordList1 | wordList2)
	

	return float( len(intersection)) / len(union)
