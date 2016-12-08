# modules with functions essential to graph traversal

# local modules
import webutils
import wikipedia as wiki
from webutils import *

# other modules
import time

def printElapsed( startTime):
	print "Elapsed Time: {:.2f} seconds".format(time.time() - startTime)


def removeBlacklisted( setLinks):
	setLinks.discard("Virtual International Authority File")
	setLinks.discard("International Standard Book Number")
	setLinks.discard("Integrated Authority File")
	setLinks.discard("Digital object identifier")
	setLinks.discard("Library of Congress Control Number")


#takes in a list of (dst, src) tuples and reorders them to go from the source to the destination and calls printPath
def printPath(pathList, dst, src):
	path = []
	dstToFind = dst
	currSource = dst # dummy assignment to flag variable to let us know when the path has been constructed completely

	# traverse list backwards, storing values
	while not currSource == src: #traversal complete
		for destination, source in pathList:
			currSource = source
			if destination == dstToFind:
				path.append((destination, source))
				pathList.remove((destination, source))
				dstToFind = source
				break

	path.reverse()

	# store new list to string
	pathStr = str(path[0][1]) + " -> " #print source (tuple item)
	for dest, source in path:
		pathStr += dest
		if dest != path[-1][0]: #destination
			pathStr += " -> "
	try:
		print "Distance: {} | {}".format( len(path), pathStr)
	except UnicodeError:
		print "Distance: {} | {}".format( len(path), pathStr.encode('ascii', errors='backslashreplace'))

			
