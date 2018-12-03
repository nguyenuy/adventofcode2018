#!/usr/bin/env python
from collections import Counter
import difflib

day = 2
file_name = "input.txt"

def process_input():
    with open (file_name, "r") as input_file:
        input = input_file.readlines()

    total_two = 0
    total_three = 0

    for i in input:
        count = dict(Counter(i))

        exactly_two = {key: value for key, value in count.items() if value == 2}
        exactly_three = {key: value for key, value in count.items() if value == 3}
        
        if bool(exactly_two):
            total_two += 1
        if bool(exactly_three):
            total_three += 1
        
    checksum = total_three * total_two
    print("The checksum is %d" % checksum)

def process_input_2():
    # Assumptions
    # 1. All strings in file are same length
    with open (file_name, "r") as input_file:
        input = input_file.readlines()

    

    for i in input:
        for j in input:
            s = difflib.SequenceMatcher(None, i, j)
        
            total_matching_positions = 0
            expected_matching_positions = len(j)-1
            for block in s.get_matching_blocks():
                total_matching_positions += block.size
            
            if total_matching_positions == expected_matching_positions:
                print("Found %s %s" % (i.rstrip(), j.rstrip()))
                common_string = ""
                for block in s.get_matching_blocks():
                    first_index = block.a
                    second_index = block.a + block.size
                    common_string = common_string + i[first_index:second_index].rstrip()
                
                print("Common string ==> %s" % common_string)
                exit()
    
        

if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input_2()