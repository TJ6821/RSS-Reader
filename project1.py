#My RSS reader and downlaoder.

import feedparser

myRss = feedparser.parse("https://nyaa.si/?page=rss")

print (myRss['feed']['title'])

