#!/usr/bin/python

import wikipedia as wiki
import similarity


from heapq import *

def traverse(src, dst):
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links

	for links in links:
		# heappush(frontier, [Jaccard(dst, link), link])
		# list is sorted by least from first, then least from second, etc.
		pass




#def getContent(title):
print wiki.page("Butterflies").summary


'''
print similarity.getJaccard(getContent("Association football"), getContent("Ball (gridiron football)"))
print similarity.getJaccard(getContent("Butterflies"), getContent("Ball (gridiron football)"))
print similarity.getJaccard(getContent("Butterflies"), getContent("Sickle Cell"))
print similarity.getJaccard(getContent("Butterflies"), getContent("January"))
'''
