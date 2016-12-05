#!/usr/bin/python

import Queue
import similarity
import sys
import traversal
import webutils
import wikipedia as wiki

if __name__ == '__main__':
	# get src and target from command line arguments
	try:
		src = sys.argv[1]
		target = sys.argv[2]
	except IndexError:
		print "usage: main.py [src] [target]"
		print "Exiting..."
		sys.exit(1)
	
	pQueue = Queue.PriorityQueue()

	# testing
	for title in webutils.getLinkTitles(src):
		ratio = similarity.getJaccard(src, title)
		try:
			#print 'Similarity between {} and {}: {}'.format(src, title, ratio)
			pQueue.put((1-ratio, title))
		except UnicodeError:
			pass
	
	while not pQueue.empty():
		try:
			print 'Up-Next: {}'.format(pQueue.get()[1])
		except UnicodeError:
			pass
