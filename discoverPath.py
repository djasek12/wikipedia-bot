# module to enable traversal of graph

import Queue
import webutils
import wikipedia as wiki
import similarity
import sys 
import time
import random
import bisect

from traversal import *
from heapq import *
from similarity import *
from webutils import *

def traverse(src, dst):
	#start the clock
	startTime = time.time()

	MAX_COMMON = 20
	MAX_RANDOM = 5
	MAX_FUTURE = 3

	# correct dst in case title is different
	dst = webutils.getTitle(dst)

	dstLinks = webutils.getLinkTitles(dst)

	# new, experimental method to find best option with ordered list
	future = []
	future += [(0, src)]

	##############################

	visited = set()

	path = [src]
	curr = src

	while curr != dst:
		print "Searching", curr.upper(), "..."

		# 1) look for direct link between src and dst
		currLinks = set(webutils.getLinkTitles(curr.lower())) - visited
		removeBlacklisted(currLinks)
	
		print "immediate find..."
		if dst.lower() in [x.lower() for x in currLinks]:
			path.append(dst)
			printElapsed(startTime)
			printPath(path)
			sys.exit(0)


		# 2) Compute Common Links
		# (intersection between links of curr and dst)
		print "common links..."

		all_common = set(currLinks) & set(dstLinks)

		# limit the number of links in common set to MAX_COMMON
		common = random.sample(all_common, min(len(all_common), MAX_COMMON))
	
		maxJaccard = 0
		title = ""

		# 3) If there are pages in common, iterate through them
		if len(common) > 0:
			for page in common:
				# 3a) get articles linked from common page
				try:
					links = webutils.getLinkTitles(page)
				except:
					continue

				# 3b) if common page points to dst, SUCCESS, end program
				if dst.lower() in [title.lower() for title in links]:
					print '\t            "{}"'.format(page)
					path.append(page)
					path.append(dst)
					printElapsed(startTime)
					printPath(path)
					sys.exit(0)
				# 3c) else, compute Jaccard between all common pages and dst and 
				# choose the lowest Jaccard
				else:
					try:
						jaccard = getJaccard(links, dstLinks)
						print '\tSimilarity: "{}" and "{}" == {}'.format(page, dst, jaccard)
					except:
						continue

					############
			
					if jaccard > future[0][0]:
						if len(future) >= MAX_FUTURE:
							future.remove(min(future))
						future += [(jaccard, page)]
					
					############

					# old method:
					if jaccard > maxJaccard:
						maxJaccard = jaccard;
						nextPage = page

		# 4) If there are no common pages between curr and dst, chose 5 random 
		# pages linked from curr, and choose one with smallest Jaccard score
		else:
			print "\tNo common pages."
			print "Random Linked Pages:"
			# there are no commonly referenced pages, so select MAX_RANDOM random
			for page in random.sample(currLinks, min(len(currLinks), MAX_RANDOM)):
				try:
					jaccard = getJaccard(getLinkTitles(page), dstLinks)
					print '\tSimilarity: "{}" and "{}" == {}'.format(page, dst, jaccard)
				except:
					continue

				##########
				if jaccard > future[0][0]:
					if len(future) >= MAX_FUTURE:
						future.remove(min(future))
					future += [(jaccard, page)]

				##########

				# old method:
				if jaccard > maxJaccard:
					maxJaccard = jaccard
					nextPage = page


		# 5) Loop through again, with newly selected page chosen by Jaccard in (3b) or (4)
		# old method:
		'''
		path.append(nextPage)
		visited.add(curr)
		curr = nextPage
		'''


		# new method:
		################
		visited.add(curr)

		curr = max(future)[1]
		future.remove(max(future))
		path.append(curr)
