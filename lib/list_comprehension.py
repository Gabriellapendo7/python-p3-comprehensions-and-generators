#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]

print(return_evens([0,1,2,3,4,5,6,7,8,9,10]))

    #using list comprehension
# evens = [n for n in range(1, 20) if n % 2 == 0]
# print(evens)  
    

def make_exclamation(sentence_list):
    return [x + "!" for x in sentence_list]

print(make_exclamation(["hey", "hello there"]))
    