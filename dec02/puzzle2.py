#!/usr/bin/python
# Advent of Code 2018
# Day 2 - Part 2 

import collections

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.readlines()

highest_match_len = len(my_input[0]) -1

for i, id in list(enumerate(my_input)):
    for id2 in my_input[i+1:]: 
        matches = ''.join(x for (x,y) in zip(id, id2) if x == y)
        if len(matches) == highest_match_len:
            print (matches)
