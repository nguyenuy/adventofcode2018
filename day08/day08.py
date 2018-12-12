#!/usr/bin/env python
import re
from collections import defaultdict
import collections

day = 7 
file_name = "input2.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input():
    print("Running problem 1")
    input = get_input()
    entries = input[0].split()
    
    root_header = entries[0:2]
    root_nodes = root_header[0]
    root_metadata = root_header[1]

    metadata_entries = []
    for i in range(0, len(entries)):
        pass

    

        




if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()

