#!/usr/bin/python
# Advent of Code 2018
# Day 1 - Part 2 

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.readlines()

found = False
frequency = list()
total = 0
while not found: 
    for line in my_input:
        if line.startswith('+'):
            total += int(line[1:])
        else:
            total -= int(line[1:])
    
        if total in frequency: 
            print (total)
            found = True 
            break
        else: 
            frequency.append(total)
        
