# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:47:07 2018

@author: Kajal
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    freq = {}
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt') 
    
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        posList=set() #list of positive words
        
        line=line.lower().strip()    
        
        words=line.split(' ') # split on the space to get list of words
   
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                posList.add(word) #update the positive list for this review 
     
        for word in posList:
            if word in freq: #word is in dictionary so increment value with 1
                freq[word] = freq[word] + 1 
            else: #word is not in dictionary so initialize value with 1
                freq[word] = 1
    fin.close()
    return freq


if __name__ == "__main__": 
    freq=run('textfile') 
    print(freq)