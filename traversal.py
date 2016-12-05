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
	print srcLinks
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
	
	print "out of Alex's"

	heappush( frontier, [0, 0, src, src]) 
	# [depth, Jaccard, src, dst]
	
	while frontier: 
		#print len(frontier)
		outpost = heappop( frontier)
		print "CHOSE :", outpost[3], "<======================================="


		# prevent loops
		if outpost[3] in marked:
			continue

		marked.add(outpost[2])
		path.add((outpost[3], outpost[2]))

		links = webutils.getLinkTitles(outpost[3])

		#
		if dst in links:
			printElapsed(startTime)
			sys.exit(0)

		for title in links:	
			try:
				jaccard = 1 - similarity.getJaccard(webutils.getLinkTitles(title), webutils.getLinkTitles(dst))
			except wiki.wikipedia.PageError:
				pass

			print 'Similarity between {} and {}: {}'.format(title, dst, jaccard)
			heappush(frontier, [jaccard, 
								outpost[0]+1,
								outpost[3],
								title])


def printElapsed( startTime):
	print "Elapsed Time: {}".format(time.time() - startTime)

def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")
	temp = u"Bibliot\xe8que nationale de France"
	setLinks.discard(temp)

def printPath( listPath):
	path = ""
	for page in listPath:
		path += page
		if page != listPath[-1]:
			path += " -> "
	
	try:
		print "Distance: {} | {}".format( len(listPath)-1, path)
	except UnicodeError:
		print "Distance: {} | {}".format( len(listPath)-1, path.encode('ascii', errors='backslashreplace'))


def constructPath(graph, dst, src):
	path = []
	curr = dst
	while curr != src:
		for edge in graph:
			if dst == edge[0]:
				curr = edge[1]
				path += curr
				break

	printPath(path.reverse())
			
