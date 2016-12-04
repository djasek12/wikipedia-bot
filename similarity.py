#!/usr/bin/python

def getJaccard( wordList1, wordList2):
	# get the union of the two lists
	intersection = list( set(wordList1) & set(wordList2))
	union = list( set(wordList1) | set(wordList2))
	

	return float( len(intersection)) / len(union)
