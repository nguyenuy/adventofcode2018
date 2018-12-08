#!/usr/bin/env python
import re
from collections import defaultdict

day = 7 
file_name = "input2.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input():
    print("Running problem 1")
    input = get_input()
   
    available_letters = set()
    requires = defaultdict(set)
    for l in input:
        regex = 'Step (.*) must be finished before step (.*) can begin'
        m = re.search(regex, l)
        requires[m.group(2)].add(m.group(1))
        available_letters.add(m.group(2))
        available_letters.add(m.group(1))

    sorted_letters = sorted(available_letters)
    while sorted_letters != set():
        break
     

if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()

