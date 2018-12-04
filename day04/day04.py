#!/usr/bin/env python
import re

day = 4
file_name = "input.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input():
    print("Running problem 1")
    input = get_input()

    unsorted_list = []
    for event in input:
        unsorted_list.append(get_event(event))
    
    from operator import itemgetter
    unsorted_list.sort(key=itemgetter("date"))
    sorted_list = unsorted_list

    current_guard = "?"
    regex = r'Guard #([0-9]+)'
    for i in sorted_list:
        contains_guard = re.search(regex, i['event'])
        if contains_guard is not None:
            current_guard = contains_guard.group(1)
        i["guard"] = current_guard
    

    # Build out List of {Date, Guard, Time Asleep} using sorted list
    current_guard = "?"
    time_asleep = []
    guard_info = {}

    minute_asleep = -1
    minute_awake = -1
    for i in sorted_list:
        if current_guard is not i["guard"]:
            current_guard = i["guard"]
            guard_info = {}
            guard_info['date'] = i['date']
            guard_info['guard'] = i['guard']
            guard_info['minute'] = [0] * 60
            time_asleep.append(guard_info)
        else:
            if "falls asleep" in i['event']:
                minute_asleep = get_minute_from_time(i['date'])
            if "wakes up" in i['event']:
                minute_awake = get_minute_from_time(i['date'])
                guard_info['minute'][minute_asleep:minute_awake] = [1]*(minute_awake-minute_asleep)
    
    
    # Find guard that sleeps the most
    guard_sleep_info = {}
    for i in time_asleep:
        if i['guard'] not in guard_sleep_info:
            guard_sleep_info[i['guard']] = sum(i['minute'])
        else: 
            guard_sleep_info[i['guard']] += sum(i['minute'])

    sleepiest_guard = max(guard_sleep_info, key=guard_sleep_info.get)

    sleep_time = [0] * 60
    for g in time_asleep:
        if g['guard'] == sleepiest_guard:
            sleep_time = [sum(x) for x in zip(sleep_time, g['minute'])]
    
    max_minute = sleep_time.index(max(sleep_time))
    ### Part 1
    print(max_minute*int(sleepiest_guard))


    ### Part 2
    guard_sleep_info = {}
    for i in time_asleep:
        if i['guard'] not in guard_sleep_info:
            sleep_time = [0] * 60
            guard_sleep_info[i['guard']] = [sum(x) for x in zip(sleep_time, i['minute'])]
        else:
            guard_sleep_info[i['guard']] = [sum(x) for x in zip(guard_sleep_info[i['guard']], i['minute'])]

    
    g_sleep_info = {}
    for k in guard_sleep_info:
        g_sleep_info[k] = max(guard_sleep_info[k])

    frequent_sleepiest_guard = max(g_sleep_info, key=g_sleep_info.get)

    max_minute = guard_sleep_info[frequent_sleepiest_guard].index(max(guard_sleep_info[frequent_sleepiest_guard]))
    print(max_minute*int(frequent_sleepiest_guard))


def get_minute_from_time(timestamp):
    regex = r'.* .*:([0-9]+)'    
    match = re.search(regex, timestamp)
    return int(match.group(1))
    


        
        
    
    
        
    


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