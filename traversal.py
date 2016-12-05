# module to enable traversal of graph

# local modules
import Queue
import webutils
import wikipedia as wiki
import similarity
import sys 

# default modules
from heapq import *


def traverse(src, dst, type="article"):
	# first, look for direct link between src and dst
	srcLinks = webutils.getLinkTitles(src)
	if dst in srcLinks:
		print "Distance: 1 | Path: {} -> {}".format(src, dst)
		sys.exit(0)

	# next, look for common link on both src and dst
	dstLinks = webutils.getLinkTitles(dst)
	common = set(srcLinks) & set(dstLinks)
	if len(common) != 0: 
		print "Distance: 2 | Path: {} -> {} -> {}".format(src, common.pop(), dst)
		sys.exit(0)

	#finally, do real traversal
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links
	path = set()
	pQueue = Queue.PriorityQueue()
	
	srcText = webutils.getSummary(src)
	dstText = webutils.getSummary(dst)
	
	linkText = ""
	for link in webutils.getLinkTitles(src):
		linkText = webutils.getSummary(link)
		ratio = similarity.getJaccard(linkText, dstText)
		pQueue.put((1-ratio), link)
		try:
			print 'Working on {}: {}'.format(link, ratio)
		except UnicodeError:
			pass
	
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

def printPath( listPages):
	for page in listPages:

