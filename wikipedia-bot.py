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
	
	# do traversal	
	try:
		traversal.traverse(src, target, "article")
	except: 
		print "Page Not Found!"
		print "Exiting"
		sys.exit(1)

