#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:54:40 2019

@author: zahash
"""


def word_count(string):
    word_list = string.strip().split(' ')
    
    unique_words_set = set()
    count_dict = {}
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
            unique_words_set.add(word)
    
    return count_dict, unique_words_set

    
def ransom(ransom_note, magazine):
    ransom_count_dict, ransom_words_set = word_count(ransom_note)
    magazine_count_dict, magazine_words_set = word_count(magazine)
    
    if len(ransom_words_set - magazine_words_set) > 0:
        return False
    
    for word in ransom_words_set:
        if ransom_count_dict[word] > magazine_count_dict[word]:
            return False
    
    return True
    


def test():
    ransom1 = 'my name is zahash'
    ransom2 = 'im zahash'
    magazine1 = 'zahash is not my name'
    magazine2 = 'zahash'
    
    assert ransom(ransom1, magazine1) == True
    assert ransom(ransom2, magazine2) == False
    
    print("ALL TESTS PASSED")

if __name__ == '__main__':
    test()
    
    
    