import wikipedia as wiki

def getLinkTitles(title):
    wikiPage = wiki.page(title)
    return wikiPage.links

def getContent(title):
    return wiki.page(title).content


