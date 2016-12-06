# module to enable traversal of graph


import Queue
import webutils
import wikipedia as wiki
import similarity
import sys 
import time
import random

from traversal import *
from heapq import *
from similarity import *
from webutils import *

def traverse(src, dst):
	#start the clock
	startTime = time.time()

	# correct dst in case title is different
	dst = webutils.getTitle(dst)

	dstLinks = webutils.getLinkTitles(dst)

	visted = set()

	path = [src]
	curr = src

	while curr != dst:
		print "Searching", curr.upper(), "..."

		# 1) look for direct link between src and dst
		currLinks = webutils.getLinkTitles(curr.lower())

		print "immediate find..."
		if dst.lower() in [x.lower() for x in currLinks]:
			path.append(dst)
			printElapsed(startTime)
			printPath(path)
			sys.exit(0)


		# 2) Compute Common Links
		# (intersection between links of curr and dst)
		print "common links..."

		common = set(currLinks) & set(dstLinks) 
		removeBlacklisted(common)
		
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

					if jaccard > maxJaccard:
						maxJaccard = jaccard;
						nextPage = page

		# 4) If there are no common pages between curr and dst, chose 5 random 
		# pages linked from curr, and choose one with smallest Jaccard score
		else:
			print "\tNo common pages."
			print "Random Linked Pages:"
			# there are no commonly referenced pages, so select 5 random
			for page in random.sample(currLinks, min(len(currLinks), 5)):
				try:
					jaccard = getJaccard(getLinkTitles(page), dstLinks)
					print '\tSimilarity: "{}" and "{}" == {}'.format(page, dst, jaccard)
				except:
					continue

				if jaccard > maxJaccard:
					maxJaccard = jaccard
					nextPage = page

		# 5) Loop through again, with newly selected page chosen by Jaccard in (3b) or (4)
		path.append(nextPage)
		curr = nextPage
