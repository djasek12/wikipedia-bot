import wikipedia as wiki

def getLinkTitles(title):
    return wiki.page(title).links

def getContent(title):
    return wiki.page(title).content

def getSummary(title):
	return wiki.page(title).summary

