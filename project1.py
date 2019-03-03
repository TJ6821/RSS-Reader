#My RSS reader and downlaoder.

import feedparser

myRss = feedparser.parse("https://nyaa.si/?page=rss")

print 'Number of RSS posts :', len(myRss.entries)
myList = myRSS.myList[1]

print 'Post Title : ',myList.title
