#!/usr/bin/env python
import re
from collections import defaultdict
import collections
import sys
from collections import deque, defaultdict

# Importing a Circular Doubly Linked List which is needed for this problem
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None

    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)

    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)

    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node

    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next

    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break
day = 9 
file_name = "input.txt"

def get_input():
    with open (file_name, "r") as input_file:
        input = input_file.read().splitlines()
    return input


def lets_get_it(players, last_marble):
    current_marble = 0
    
    # Initialize Data Structures
    my_list = CircularDoublyLinkedList()
    
    current_node = Node(current_marble) 
    my_list.insert_at_end(current_node)

    # Initialize player's scores to 0
    scores = [0] * players
    
    while True:
        current_marble += 1
        current_player = (current_marble) % players
        
        if current_marble % 23 is 0:
            scores[current_player] += current_marble
            node_to_remove = current_node
            for i in range(0,7):
                node_to_remove = node_to_remove.prev
                i += 1
            
            scores[current_player] += node_to_remove.data
            current_node = node_to_remove.next
            my_list.remove(node_to_remove)
        else:
            node_to_add = Node(current_marble)
            node_to_add_right_of = current_node        
            for i in range(0,1):
                node_to_add_right_of = node_to_add_right_of.next
                i += 1 

            my_list.insert_after(node_to_add_right_of, node_to_add)
            current_node = node_to_add

        if current_marble == last_marble:
            print(max(scores))
            break




if __name__ == '__main__':
    print("Executing day %d code...." % day)
    print("Running problem 1")
    
    players = 479 
    last_marble = 71035*100
    lets_get_it(players, last_marble)



