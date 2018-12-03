#!/usr/bin/env python
from collections import Counter

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
        

if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()