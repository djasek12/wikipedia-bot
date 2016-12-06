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
from similarity import *
from webutils import *

def traverse(src, dst, path):	
	print path

	#start the clock
	startTime = time.time()

	# first, look for direct link between src and dst
	srcLinks = webutils.getLinkTitles(src)


	if dst.lower() in [x.lower() for x in srcLinks]:
		takenpath = [src]
		takenpath.append(dst)
		printElapsed(startTime)
		printPath(path.split() + takenpath)
		sys.exit(0)

	# next, look for common link on both src and dst
	dstLinks = webutils.getLinkTitles(dst)
	common = set(srcLinks) & set(dstLinks)
	removeBlacklisted(common)
	
	if len(common) != 0:
		for i in range( 0, len(common)):
			takenpath = [src]
			page = common.pop()
			if dst.lower() in [x.lower() for x in webutils.getLinkTitles(page)]:
				takenpath.append(page)
				takenpath.append(dst)
				printElapsed(startTime)
				printPath(path.split() + takenpath)
				sys.exit(0)

	max = 0
	title = ""
	for link in srcLinks:
		#find its jaccard similarity with dst 
		jaccard = getJaccard(getLinkTitles(link), dstLinks)

		if jaccard > max:
			max = jaccard;
			title = link
	
	traverse(title, dst, path+" "+src)

	'''	
	#finally, do real traversal
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links
	path = set()
	

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

			try:
				print 'Similarity between {} and {}: {}'.format(title, dst, jaccard)
				heappush(frontier, [jaccard, 

								outpost[0]+1,
								outpost[3],
								title])
			except:
				pass
	'''


def printElapsed( startTime):
	print "Elapsed Time: {:.2f} seconds".format(time.time() - startTime)

def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")
	setLinks.discard("Integrated Authority File")
	setLinks.discard("Digital object identifier")
	setLinks.discard("Library of Congress Control Number")

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
			
