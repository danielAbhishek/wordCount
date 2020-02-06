from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()

    wordCountDict = {}

    for word in wordList:
        if word in wordCountDict:
            #increase
            wordCountDict[word] += 1
        else:
            #addToDict
            wordCountDict[word] = 1

    sortedWords = sorted(wordCountDict.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fullText' : fullText, 'count': len(wordList), 'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')