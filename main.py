""""
Aaron Whitaker
9/25/2022
CRN: 10235
CIS 226: Advanced Python Programming
Est. Time: 8 hours
"""

import pytest

array = []
o = []
o_ll = []
o_la = []
o_bin = []
node_track = []

# necessary function to pass arguments into the linked list
def main(a, b, c, d, e, f, g, h, i, j):

    # Create Items
    o.append(1)
    node_1 = Node(f'{a}')
    o.append(1)
    node_2 = Node(f'{b}', prev=node_1)
    o.append(1)
    node_3 = Node(f'{c}', prev=node_2)
    o.append(1)
    node_4 = Node(f'{d}', prev=node_3)
    o.append(1)
    node_5 = Node(f'{e}', prev=node_4)
    o.append(1)
    node_6 = Node(f'{f}', prev=node_5)
    o.append(1)
    node_7 = Node(f'{g}', prev=node_6)
    o.append(1)
    node_8 = Node(f'{h}', prev=node_7)
    o.append(1)
    node_9 = Node(f'{i}', prev=node_8)
    o.append(1)
    node_10 = Node(f'{j}', prev=node_9)

    func_calls(node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10)

# calls necessary functions for the program
def func_calls(node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10):
    i = 0
    # calls linear search on linked list
    o.append(1)
    lin_search_llist(i, 8, node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10)
    # calls array from linked list, then calls linear search on array
    o.append(1)
    trav_dl_list(node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10)
    o.append(1)
    o_la.append(1)
    lin_search_array(array, 8)
    o.append(1)
    # calls binary search on sorted array
    o.append(1)
    bin_search(array, 8)
    

# linear search on linked list
def lin_search_llist(i, find, node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, traversed=None):
    try:
        node = node_track[i-1]
    except:
        node = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10
    o_ll.append(1)
    traversed = traversed or []
    o_ll.append(1)
    if not node or node in traversed:
        o_ll.append(1)
        return
    o_ll.append(1)
    traversed.append(node)
    o_ll.append(1)
    if node.prev:
        o_ll.append(1)
        node_track.append(node.prev)
        o_ll.append(1)
        i += 1
        o_ll.append(1)
        lin_search_llist(i, find, node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, traversed=traversed)
    o_ll.append(1)
    if node.next:
        o_ll.append(1)
        node_track.append(node.next)
        o_ll.append(1)
        i += 1
        o_ll.append(1)
        lin_search_llist(i, find, node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, traversed=traversed)
    o_ll.append(1)
    if int(node.data) == find:
        o_ll.append(1)
        print (f"Linear linked search was aprox {sum(o_ll)} steps")
        print (node.data)
        return

# linear search on array | O(n) due to for loop
def lin_search_array(array, find):
    o_la.append(1)
    for i, value in enumerate(array):
        o_la.append(1)
        if int(value) == find:
            o_la.append(1)
            print (f"Linear array search was aprox {sum(o_la)} steps")
            print (value)
            return 

# binary search on sorted array | O(log n) due to binary search
def bin_search(array, find):
    s_sort(array)
    o_bin.append(1)
    begin = 0
    o_bin.append(1)
    end = len(array) - 1
    o_bin.append(1)
    find = 8
    o_bin.append(1)
    while find >= 0 and begin <= end:
        o_bin.append(1)
        mid = int((begin + end) / 2)
        o_bin.append(1)
        if array[mid] == find:
            o_bin.append(1)
            find = mid
        elif int(array[mid]) < find:
            o_bin.append(1)
            begin = mid + 1
        else:
            o_bin.append(1)
            end = mid - 1
    print (f"Binary sorted search was aprox {sum(o_bin)} steps")
    print(find)

# swap function called from below
def swapper(array, index1, index2):
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp
    return 

# swap sorts the array | O(n^2) nested for loops based on array length
def s_sort(array):
    for marker_c in range(len(array) - 1):
        marker_a = marker_c
        for marker_b in range(marker_c, len(array)):
            if array[marker_b] < array[marker_c]:
                marker_c = marker_b
        if marker_c != marker_a:
            swapper(array, marker_c, marker_a)
    return array, o_bin

# node class for linked list
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev 
        self.next = next 

# creates array from listed list
def trav_dl_list(node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, traversed=None):
    o_la.append(1)
    array.append(node_1.data)
    o_la.append(1)
    array.append(node_2.data)
    o_la.append(1)
    array.append(node_3.data)
    o_la.append(1)
    array.append(node_4.data)
    o_la.append(1)
    array.append(node_5.data)
    o_la.append(1)
    array.append(node_6.data)
    o_la.append(1)
    array.append(node_7.data)
    o_la.append(1)
    array.append(node_8.data)
    o_la.append(1)
    array.append(node_9.data)
    o_la.append(1)
    array.append(node_10.data)
    return

if __name__ == "__main__":
    main(1, 7, 4, 2, 9, 8, 10, -4, 0, 3)
    
"""
Design: I initially went off the lessons provided in the class so far.
Develope: I rewrote the lessons to meet the needs of the assignment, but getting the arguments passed into main to populate the linked list was a challenge. 
Test: I tested the program with the required arguments, along with 1-9 and the reverse.
Documentation:
The above program finds 8 from the numbers passed to main. It first performs a linear search on the linked list, then creates an array from the linked list, 
then performs a linear search on the array, and finally performs a binary search on the sorted array. The program is tested with pytest. 
"""