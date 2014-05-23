from __future__ import print_function
import re
import json


titleExpr = re.compile("<title>.*</title>") 
linkExpr = re.compile('\[\[(.+?)\]\]')

articleDump = open("wikipedia.xml", "r", 1)
articles = dict()

i = 0
for line in articleDump:
    titleMatch = titleExpr.search(line)
    linkMatches = linkExpr.findall(line)
    if titleMatch is not None:
        i += 1
        if i % 100000 == 0:
            print("Processed", i, "articles")
            with open("tmp/" + str(i) + ".json", 'wb') as f:
                json.dump(articles, f, ensure_ascii=False)
            articles = dict()
        curTitle = titleMatch.group()[7:len(titleMatch.group())-8]
        articles[curTitle] = []
           
    for match in linkMatches:
        articles[curTitle].append(match)

print("Saving last file...")
with open("/tmp/" + str(i) + ".json", "wb") as f:
    json.dump(articles, f)

print("Done!")

