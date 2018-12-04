#!/usr/bin/python
# Advent of Code 2018
# Day 1 - Part 1 

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.readlines()

total = 0
for line in my_input:
    if line.startswith('+'):
        total += int(line[1:])
    else:
        total -= int(line[1:])

print (total)
