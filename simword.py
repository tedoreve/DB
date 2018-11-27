# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:36:58 2018

@author: tedoreve
"""

from nltk.corpus import words
from nltk.corpus import wordnet
import difflib
from googletrans import Translator
import sqlite3 as db
from functools import reduce

#==============================================================================

def similar(word, n, cutoff, Google):
    dic  = words.words()
    sim  = difflib.get_close_matches(word, dic, n = n, cutoff = cutoff)    
    # func = lambda x,y:x if y in x else x + [y]
    # sim  = reduce(func, [[], ] + sim)
    
    print('')
    
    if Google:
        translator1   = Translator()
        translations = translator1.translate(sim,dest='zh-cn')
        for translation in translations:
            print(translation.origin, ' '*(13-len(translation.origin))+'-> ', translation.text)
    else:
        conn = db.connect('Mydict.db')
        cursor = conn.cursor()
        conn.row_factory = db.Row
        cursor.execute("select * from stardict")
        rows = cursor.fetchall()
        translator2 = dict(rows)
        for word in sim:
            try:
                print(word, ' '*(13-len(word))+'-> ', translator2[word])
            except:
                continue
    print('')

    return sim
    
#==============================================================================

def meaning(sim):
    synonyms = []
    
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
                 synonyms.append(lm.name())
    print (set(synonyms))
    
    antonyms = []
    
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())
    
    print(set(antonyms))
    return '有空做个APP'
    
#==============================================================================
if __name__ == '__main__':
    word   = 'moral'  
    n      = 100          #upper limit number of similar words
    cutoff = 0.75         #larger value means less words
    Google = False
    sim    = similar(word, n, cutoff, Google)
    app    = meaning(sim)