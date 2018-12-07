#!/usr/bin/env python
import re
from operator import itemgetter
from pprint import pprint

day = 6
file_name = "input.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input
    
def process_input():
    print("Running problem 1")
    input = get_input()

    coordinates = []
    for i in input:
        point = i.split(",")
        x = int(point[0])
        y = int(point[1].rstrip())
        coordinates.append((x,y))

    ## Assumptions edges of matrix go on forever
    matrix_size = (max(coordinates))
    distances = [["." for i in range(matrix_size[0]+2 )] for j in range(matrix_size[1]+2)]
    total_distances = [["." for i in range(matrix_size[0]+2 )] for j in range(matrix_size[1]+2)]

    for i in range(0, len(distances)):
        for j in range(0, len(distances[0])):
            shortest_distance = 1000000000
            duplicate_distance = 1000000000
            total_distance = 0 
            for x in coordinates:
                distance = get_manhattan_distance(x, (i,j))
                total_distance += distance
                if distance < shortest_distance:
                    shortest_distance = distance
                    distances[i][j] = "x" + str(x[0]) + "y" + str(x[1])
                    # print(str(i) + " " + str(j))  + " ----> " +  str(x)
                elif shortest_distance == distance:
                    # print(str(i) + " " + str(j))  + " ----> " +  "." + " <--- " + str(x)
                    duplicate_distance = distance
            if duplicate_distance == shortest_distance:
                distances[i][j] = "...."
            total_distances[i][j] = total_distance
    #pprint(distances)

    area = 0
    less_than = 10000
    for i in range(0, len(distances)):
        for j in range(0, len(distances[0])):
            if total_distances[i][j] < less_than:
                area += 1
    
    print(area)
    # Ignore Distances
    ignore_distances = set()
    ignore_distances.add('....')
    for i in distances[0]:
        ignore_distances.add(i)
    for i in distances[-1]:
        ignore_distances.add(i)

    for i in distances:
        ignore_distances.add(i[0])
        ignore_distances.add(i[-1])
    
    finite_size = {}
    for i in range(0, len(distances)):
        for j in range(0, len(distances[0])):
            if distances[i][j] not in ignore_distances:
                if distances[i][j] not in finite_size:
                    finite_size[distances[i][j]] = 1
                else:
                    finite_size[distances[i][j]] += 1

    import operator
    max_key = max(finite_size.iteritems(), key=operator.itemgetter(1))[0]
    print(finite_size[max_key]) 
    print(part2(input))

def get_manhattan_distance(coorda, coordb):
    return abs(coorda[0]-coordb[0]) + abs(coorda[1]-coordb[1])


def part2(lines, manhattan_limit=10000):
    coords = set()
    max_r = max_c = 0

    for line in lines:
        r, c = map(int, line.split(", "))
        coords.add((r, c))
        max_r = max(max_r, r)
        max_c = max(max_c, c)

    size_shared_region = 0

    for i in range(max_r + 1):
        for j in range(max_c + 1):
            size_shared_region += int(sum(abs(r - i) + abs(c - j) for r, c in coords) < manhattan_limit)

    return size_shared_region

if __name__ == '__main__':
    print("Executing day %d code...." % day)
    process_input()