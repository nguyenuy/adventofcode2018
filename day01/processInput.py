#!/usr/bin/env python

file_name = "input.txt"
starting_input = 0
resulting_frequencies = set() # Initialize list

def process_input():
    running_counter = starting_input
    resulting_frequencies.add(starting_input)
    while True:
        with open (file_name, "r") as input_file:
            for line in input_file:
                value = get_absolute_value(line)
                if is_negative(line):
                    running_counter = running_counter - value
                else:
                    running_counter = running_counter + value
                
                if running_counter in resulting_frequencies:
                    print("We found you: %d" % running_counter)
                    exit()
                else:
                    resulting_frequencies.add(running_counter)
        
        #print("The value is %d", running_counter)

def is_negative(number):
    sign = number[0]
    return sign is '-'

def get_absolute_value(number):
    return int(number[1:])    

if __name__ == '__main__':
    print("Hello there")
    process_input()