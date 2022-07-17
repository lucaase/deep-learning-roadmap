# Text processing with urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    print(line.decode().strip())

# Put the web data into a dictionary

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# Web scraping with beautifulsoup
html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

