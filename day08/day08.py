#!/usr/bin/env python
import re
from collections import defaultdict
import collections
import sys

sys.setrecursionlimit(1000000)

day = 7 
file_name = "input.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input(tree):
    #print("here")
    #print(tree)
    root_nodes, root_metadata = tree[:2]

    total_metadata = 0
    remaining_tree = tree[2:]
    
    # Terminating condition
    total_metadata_sum = 0
    for i in range(0, root_nodes):
        #print("here2")
        #print(remaining_tree)
        metadata_sum, remaining_tree = process_input(remaining_tree)
        total_metadata += metadata_sum
    
    total_metadata += sum(remaining_tree[:root_metadata])

    return total_metadata, remaining_tree[root_metadata:]

def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, data = parse(data)
        totals += total

    totals += sum(data[:metas])

    return (totals, data[metas:])


if __name__ == '__main__':
    print("Executing day %d code...." % day)
    print("Running problem 1")
    
    input = get_input()
    entries = input[0].split()
    entries = [int(i) for i in entries]
    x = process_input(entries)
    print(x[0])
    print(process_input([0, 3, 1, 1, 1]))

    total, remaining = parse(entries)

    print('part 1:', total, remaining)
 

