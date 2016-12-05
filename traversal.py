# module to enable traversal of graph

# local modules
import Queue
import webutils
import wikipedia as wiki
import similarity
import sys 
import time 

# default modules
from heapq import *


def traverse(src, dst, type="article"):	
	#start the clock
	startTime = time.time()

	# first, look for direct link between src and dst
	srcLinks = webutils.getLinkTitles(src)
	if dst.lower() in [x.lower() for x in srcLinks]:
		path = [src]
		path.append(dst)
		printElapsed(startTime)
		printPath(path)
		sys.exit(0)

	# next, look for common link on both src and dst
	dstLinks = webutils.getLinkTitles(dst)
	common = set(srcLinks) & set(dstLinks)
	removeBlacklisted(common)
	
	if len(common) != 0:
		for i in range( 0, len(common)):
			path = [src]
			page = common.pop()
			if dst.lower() in [x.lower() for x in webutils.getLinkTitles(page)]:
				path.append(page)
				path.append(dst)
				printElapsed(startTime)
				printPath(path)
				sys.exit(0)
	
	#finally, do real traversal
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links
	path = set()
	
	heappush( frontier, [0, 0, src, src]) 
	# [depth, Jaccard, src, dst]
	
	while frontier: 
		outpost = heappop( frontier)
		
		# prevent loops
		if outpost[2] in marked:
			continue

		marked.add(outpost[2])
		path.add((outpost[3], outpost[2]))

		links = webutils.getLinkTitles(outpost[3])

		if dst in links:
			printElapsed(startTime)
			sys.exit(0)

		for link in links:	
			heappush(frontier, [outpost[0]+1, similarity.getJaccard(dst, link), outpost[2], link])



def printElapsed( startTime):
	print "Elapsed Time: {}".format(time.time() - startTime)

def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")

def printPath( listPath):
	path = ""
	for page in listPath:
		path += page
		if page != listPath[-1]:
			path += " -> "
	try:
		print "Distance: {} | {}".format( len(listPath)-1, path)
	except UnicodeError:
		pass

