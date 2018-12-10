#!/usr/bin/env python
import re
from collections import defaultdict
import collections

day = 7 
file_name = "input.txt"

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

    for i in available_letters:
        if i not in requires:
            requires[i] = set()

    sorted_letters = sorted(available_letters)
    sorted_requires = collections.OrderedDict(sorted(requires.items()))
    output = []
    while bool(sorted_requires):
        for k,v in sorted_requires.items():
            if v - set(output) == set():
                output.append(k)
                sorted_requires.pop(k)
                break

    ## Part 1
    print("".join(output))
    
    ## Edit these values
    base_time = 60
    current_time = 0 
    number_workers = 5
   
    letters_processed = set()
    letters_to_process = output.copy()
    workers_processing = {}
    while set(letters_processed) != set(output):
        # Check if workers have work expired
        workers_to_remove = set()
        for k,v in workers_processing.items():
            if v == current_time:
                letters_processed.add(k)
                letters_to_process.remove(k)
                workers_to_remove.add(k)
        
        for i in workers_to_remove:
            workers_processing.pop(i)

        # Add work to workers
        for i in letters_to_process:
            if len(workers_processing) < number_workers:
                if i not in workers_processing:
                    if (requires[i] - letters_processed) == set():
                        workers_processing[i] = current_time + base_time + ord(i) - ord('A') + 1
       
        current_time += 1
    
    print(current_time - 1) #counter counts up one more time
        

        




if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()

