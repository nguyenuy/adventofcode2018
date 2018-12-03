#!/usr/bin/env python
import re

day = 3
file_name = "input.txt"


def process_input_2():
    input = get_input()
        

def extract_claim_info(claim_string):
    regex = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
    matches = re.search(regex, claim_string)
    
    claim_info = {}

    claim_info["claim_number"] = int(matches.group(1))
    claim_info["start_x"] = int(matches.group(2))
    claim_info["start_y"] = int(matches.group(3))
    claim_info["width"] = int(matches.group(4))
    claim_info["length"] = int(matches.group(5))

    return claim_info

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    
    return input

def process_input():
    print("Running problem 1")
    input = get_input()
    matrix = []
    for x in range(1000):
        matrix.append([0]*1000)

    colliding = []
    colliding_ids = []
    all_ids = []
    for x in input:
        label,l,t,w,h = [int(y) for y in re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', x).groups()]
        all_ids.append(label)
        for o in range(h):
            for i in range(w):
                current = matrix[t+o][l+i]
                if current != 0:
                    #print("Found: %s" % current)
                    colliding.append((t+o,l+i))
                    colliding_ids.extend([current, label])
                else:
                    matrix[t+o][l+i] = label

    print(len(set(colliding)))

    print(set(all_ids) - set(colliding_ids))
    
if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()