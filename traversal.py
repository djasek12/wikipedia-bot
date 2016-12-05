# module to enable traversal of graph

# local modules
import wikipedia as wiki
import similarity

# default modules
from heapq import *


def traverse(src, dst):
	frontier = [] # heap containing the next locations to go to
	marked = set() # contains all visited links
	path = set()

	heappush( frontier, [0, getJaccard(dst, link), src, src]) 
	# [dist, jaccard, src, dst]

	while heappush: # (is not empty)

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
