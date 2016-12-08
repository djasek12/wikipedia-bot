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


def printElapsed( startTime):
	print "Elapsed Time: {:.2f} seconds".format(time.time() - startTime)

def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")
	setLinks.discard("Integrated Authority File")
	setLinks.discard("Digital object identifier")
	setLinks.discard("Library of Congress Control Number")

def printPath( listPath):
	path = str(listPath[0][1]) + " -> " #print source (tuple item)
	for dest, source in listPath:
		path += dest
		if dest != listPath[-1][0]: #destination
			path += " -> "
	
	try:
		print "Distance: {} | {}".format( len(listPath), path)
	except UnicodeError:
		print "Distance: {} | {}".format( len(listPath), path.encode('ascii', errors='backslashreplace'))


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

#takes in a list of (dst, src) tuples and reorders them to go from the source to the destination and calls printPath
def printPath2(pathList, dst, src):
        path = []
        dstToFind = dst
        currSource = dst # dummy assignment to flag variable to let us know when the path has been constructed completely

        while not currSource == src: #traversal complete
            for destination, source in pathList:
                currSource = source
                if destination == dstToFind:
                    path.append((destination, source))
                    pathList.remove((destination, source))
                    dstToFind = source
                    break

        path.reverse()
        printPath(path)



			
