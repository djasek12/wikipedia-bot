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
	if dst in srcLinks:
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
			if dst in webutils.getLinkTitles(page):
				path.append(page)
				path.append(dst)
				printElapsed(startTime)
				printPath(path)
				sys.exit(0)
	
	#finally, do real traversal
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links
	path = set()
	
	
	'''
	while heappush: 

		outpost = heappop()
		
		if outpost[2] in marked:
			continue

		marked.insert(outpost[2])
		path.insert(output[3], outpost[2])

		lisks = getList(output[3])

		if dst in links:
			marked.insert(output[3], dst)
			return True;

		#for link in getLinks(outpost[3])	
			#heappush(frontier, [Jaccard(dst, link), link])
		'''

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

