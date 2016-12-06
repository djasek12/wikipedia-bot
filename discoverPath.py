# module to enable traversal of graph

# local modules
import Queue
import webutils
import wikipedia as wiki
import similarity
import sys 
import time
import random

# default modules
from heapq import *
from similarity import *
from webutils import *

def traverse(src, dst):
	#start the clock
	startTime = time.time()

	dstLinks = webutils.getLinkTitles(dst)

	visted = set()

	path = [src]
	curr = src

	while curr != dst:
		print "Searching", curr.upper(), "..."

		# first, look for direct link between src and dst
		srcLinks = webutils.getLinkTitles(curr.lower())

		print "immediate find..."
		if dst.lower() in [x.lower() for x in srcLinks]:
			path.append(dst)
			printElapsed(startTime)
			printPath(path)
			sys.exit(0)


		# next, look for common link on both src and dst

		intersection = set(srcLinks) & set(dstLinks) 
		removeBlacklisted(intersection)
		
		print "common links..."

		# and check if any pages in common link to dst
		if len(intersection) != 0:
			for page in intersection:
				print page
				# get articles linked from page
				try:
					links = webutils.getLinkTitles(page)
				except:
					continue
				if dst.lower() in [title.lower() for title in links]:
					path.append(page)
					path.append(dst)
					printElapsed(startTime)
					printPath(path)
					sys.exit(0)

		max = 0
		title = ""

		# choose whether to use common intersection information or 
		# random selection from the srcLinks



		if (len(intersection) > 0):
			linksToSearch = intersection
			print "bad"
		else:
			linksToSearch = random.sample(srcLinks, min(len(srcLinks), 5))
			# search a maxmimum of 5 randomly chosen nodes
			print "good"

		for link in linksToSearch:
			#find its jaccard similarity with dst 
			try:
				jaccard = getJaccard(getLinkTitles(link), dstLinks)
				print 'Similarity between {} and {}: {}'.format(link, dst, jaccard)
			except:
				continue

			if jaccard > max:
				max = jaccard;
				title = link
		


		path.append(title)
		curr = title # set the next item to begin search from

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
	print "Elapsed Time: {}".format(time.time() - startTime)

def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")
	setLinks.discard("Integrated Authority File")
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
