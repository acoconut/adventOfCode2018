#!/usr/bin/python
# Advent of Code 2018
# Day 2 - Part 1 

import collections

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.readlines()

two = 0
three = 0
for line in my_input:
    counter = collections.Counter(line)
    if 2 in counter.values():
        two += 1
    if 3 in counter.values():
        three += 1

total = two * three
print (total)
