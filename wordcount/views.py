from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(req):
    return render(req,"home.html")

def count(req):
    fulltext = req.GET["fulltext"]
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(req,"count.html",{'fulltext':fulltext, 'count': len(wordlist), 'sortedWords':sortedWords })

def about(req):
    return render(req,"about.html")