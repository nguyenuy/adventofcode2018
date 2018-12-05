#!/usr/bin/env python
import re
from string import ascii_lowercase

day = 5
file_name = "input.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input():
    print("Running problem 1")
    input = get_input()
    ## Problem 1
    print(react(input[0]))

    ## Problem 2 
    polymer_length = {}
    for c in ascii_lowercase:
        print(c)
        polymer = input[0]
        print(c)
        updated_polymer = polymer.replace(c, "")
        updated_polymer = updated_polymer.replace(c.upper(), "")
        polymer_length[c] = react(updated_polymer)

    smallest_polymer = min(polymer_length, key=polymer_length.get)
    print(polymer_length[smallest_polymer])

## TODO: Optimize this function. The reaction is way too slow
def react(polymer):
    line = polymer 
    while True:
        found = False
        for i in range(0, len(line)-1):
            if line[i].lower() == line[i+1].lower():
                isFirstLower = line[i].islower()
                isSecondLower = line[i+1].islower()
                if isFirstLower and isSecondLower != True:
                    line = line[:i] + line[i+2:]
                    found = True
                    break
                elif isFirstLower is not True and isSecondLower:
                    line = line[:i] + line[i+2:]
                    found = True
                    break

        if found is False:
            break
    
    return len(line)

def get_event(input):
    event_dict = {}
    regex = r'\[(.*)\] (.*)'
    matches = re.search(regex, input)
    
    date = matches.group(1)
    event = matches.group(2)

    event_dict["date"] = date
    event_dict["event"] = event

    return event_dict

if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()