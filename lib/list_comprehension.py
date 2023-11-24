#!/usr/bin/env python3

def return_evens(num_list):
    for n in range(0,11):
        return[element for element in num_list if element % 2==0]
    pass

def make_exclamation(sentence_list):
    return[sentence + "!" for sentence in sentence_list]
    pass