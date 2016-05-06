# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:11:23 2016

@author: jonman
"""
import IPython, collections



word = open('dictionary.txt')
wordlist = word.readlines()


#print(wordlist[:20])
#print()


length = len(wordlist)
#print(length)
#print()


# Strip off the newlines
clean_words = [w.strip().lower() for w in wordlist]
#print(clean_words[:20])
#print()


# Remove dups
sorted_words = sorted(list(set([w.strip().lower() for w in wordlist])))
#print("Printing 50")
#print(sorted_words[:50])
#print()


# Join the sorted chars back into a word
def signature(s_word):
    return ''.join(sorted(s_word))
    
# Test signature()
#print(signature('lives'))


# Validate that the a_word matches the signature word
def anagram(a_word):
    return [word for word in clean_words if signature(word) == signature(a_word)]


# Test anagram()
print(anagram('jump'))
print()

words_sig = collections.defaultdict(list)

# Add all signature words will have a signature key
#   with a list of words as values that match
for word in clean_words:
    words_sig[signature(word)].append(word)
    
# This holds everything... big dictionary!
#print(words_sig)
    
    
# Function to search the dictionary for the word
#   being passed
def new_anagram(a_word):
    return words_sig[signature(a_word)]
    
    
print(new_anagram('live'))




#fh = open("/Users/jonman/Desktop/text.txt")
#words = fh.readlines()
#
#print(len(words))
#
#
#print(words[:5])
#
#
#for line in words:
#    print(line.strip().lower())
#    
#
#clean = [w.strip().lower() for w in words]
#print(clean)