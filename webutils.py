# utility funcitons to interface with the wikipedia module and 
# return the desired data

import wikipedia as wiki

def getLinkTitles(title):
	return wiki.page(title).links

def getContent(title):
	return wiki.page(title).content

def getSummary(title):
	return wiki.summary(title, 2)

def getTitle(title):
	return wiki.page(title).title

