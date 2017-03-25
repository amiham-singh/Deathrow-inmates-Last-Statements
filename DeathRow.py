
from bs4 import BeautifulSoup
import requests

import re

statements = []
url = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")
for a in soup.find_all('a', href=True):
    statements.append(a['href'])
    


p = re.compile('.*last\.html')

links = []

for link in statements:
    if p.match(link):
        links.append(link)

for link in links:
     
    url2 = "http://www.tdcj.state.tx.us/death_row/"+ link

    r2 = requests.get(url2)
    
    data2 = r2.text
    
    soup2 = BeautifulSoup(data2, "html.parser")    
    
    
    table = soup2.findAll('div', id='body')
    for x in table:
        text = x.text
        
    with open('myfile.txt', 'a') as f:
        f.write(text.split("Last Statement:")[1])




#%%

import nltk
from nltk import FreqDist
from	nltk.corpus	import	PlaintextCorpusReader
mycorpus	=	PlaintextCorpusReader('.',	'.*\.txt')
laststate	=	mycorpus.raw('Statements.txt')

file_content = open("myfile.txt").read()
tokens = nltk.word_tokenize(file_content)
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append("it's")
stopwords.append("he's")
stopwords.append("she's")
#%%
Ltokens = [x.lower() for x in tokens]
alpha=	[w	for	w	in	Ltokens	if	w.isalpha()]
words = [x for x in alpha if x not in stopwords]
dist = FreqDist(words)
freq50 = dist.most_common(50)

for x in freq50:
    print(x)