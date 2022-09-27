""""
Aaron Whitaker
9/25/2022
CRN: 10235
CIS 226: Advanced Python Programming
Est. Time: 8 hours
"""

import pytest

array = []

# necessary function to pass arguments into the linked list
def main(a, b, c, d, e, f, g, h, i, j):

    array = []

    o = 4
    o_ll = 0
    o_la = 0
    o_bin = 0

    # calls necessary functions for the program
    def func_calls(o, o_ll, o_la, o_bin):
        o_ll = o + 1
        # calls linear search on linked list
        lin_search_llist(o_ll, node_1, find=8)
        o_la = o + 2
        # calls array from linked list, then calls linear search on array
        trav_dl_list(o_la, node_1)
        lin_search_array(o_la, array, 8)
        # calls binary search on sorted array
        o_bin = o + 1
        bin_search(o_bin, array, 8)
        
    # linear search on linked list
    def lin_search_llist(o_ll, node, find, traversed=None):
        o_ll = o_ll + 1
        traversed = traversed or []
        o_ll = o_ll + 1
        if not node or node in traversed:
            o_ll = o_ll + 1
            return
        o_ll = o_ll + 1
        traversed.append(node)
        o_ll = o_ll + 1
        if node.prev:
            o_ll = o_ll + 1
            lin_search_llist(o_ll, node.prev, find, traversed=traversed)
        o_ll = o_ll + 1
        if node.next:
            o_ll = o_ll + 1
            lin_search_llist(o_ll, node.next, find, traversed=traversed)
        o_ll = o_ll + 1
        if int(node.data) == find:
            o_ll = o_ll + 1
            print (f"Linear linked search was aprox {o_ll} steps")
            print (node.data)
            return

    # linear search on array | O(n) due to for loop
    def lin_search_array(o_la, array, find):
        o_la = o_la + 1
        for i, value in enumerate(array):
            o_la = o_la + 1
            if int(value) == find:
                o_la = o_la + 1
                print (f"Linear array search was aprox {o_la} steps")
                print (value)
                return 

    # binary search on sorted array | O(log n) due to binary search
    def bin_search(o_bin, array, find):
        o_bin = o_bin + 1
        s_sort(o_bin, array)
        o_bin = o_bin + 1
        begin = 0
        o_bin = o_bin + 1
        end = len(array) - 1
        o_bin = o_bin + 1
        find = 8

        o_bin = o_bin + 1
        while find <= 0 and begin <= end:
            o_bin = o_bin + 1
            mid = int((begin + end) / 2)
            o_bin = o_bin + 1
            if array[mid] == find:
                o_bin = o_bin + 1
                find = mid
            elif array[mid] < find:
                o_bin = o_bin + 1
                begin = mid + 1
            else:
                o_bin = o_bin + 1
                end = mid - 1
        print (f"Binary sorted search was aprox {o_bin} steps")
        print(find)

    # swap function called from below
    def swapper(o_bin, array, index1, index2):
        o_bin = o_bin + 1
        temp = array[index2]
        o_bin = o_bin + 1
        array[index2] = array[index1]
        o_bin = o_bin + 1
        array[index1] = temp
        return o_bin

    # swap sorts the array | O(n^2) nested for loops based on array length
    def s_sort(o_bin, array):
        o_bin = o_bin + 1
        for marker_c in range(len(array) - 1):
            o_bin = o_bin + 1
            marker_a = marker_c
            o_bin = o_bin + 1
            for marker_b in range(marker_c, len(array)):
                o_bin = o_bin + 1
                if array[marker_b] < array[marker_c]:
                    o_bin = o_bin + 1
                    marker_c = marker_b
            o_bin = o_bin + 1
            if marker_c != marker_a:
                o_bin = o_bin + 1
                swapper(o_bin, array, marker_c, marker_a)
        return array, o_bin

    # node class for linked list
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev 
            self.next = next 

    # creates array from listed list
    def trav_dl_list(o_la, node, traversed=None):
        o_la = o_la + 1
        traversed = traversed or []
        o_la = o_la + 1
        if not node or node in traversed:
            return o_la
        o_la = o_la + 1
        traversed.append(node)
        o_la = o_la + 1
        if node.prev:
            o_la = o_la + 1
            trav_dl_list(o_la, node.prev, traversed=traversed)
        o_la = o_la + 1
        array.append(node.data)
        o_la = o_la + 1
        if node.next:
            o_la = o_la + 1
            trav_dl_list(o_la, node.next, traversed=traversed)
        return o_la

    # Create Items
    o = o + 1
    node_1 = Node(f'{a}')
    o = o + 1
    node_2 = Node(f'{b}', prev=node_1)
    o = o + 1
    node_3 = Node(f'{c}', prev=node_2)
    o = o + 1
    node_4 = Node(f'{d}', prev=node_3)
    o = o + 1
    node_5 = Node(f'{e}', prev=node_4)
    o = o + 1
    node_6 = Node(f'{f}', prev=node_5)
    o = o + 1
    node_7 = Node(f'{g}', prev=node_6)
    o = o + 1
    node_8 = Node(f'{h}', prev=node_7)
    o = o + 1
    node_9 = Node(f'{i}', prev=node_8)
    o = o + 1
    node_10 = Node(f'{j}', prev=node_9)

    # Link up Items
    o = o + 1
    node_1.next = node_2
    o = o + 1
    node_2.next = node_3
    o = o + 1
    node_3.next = node_4
    o = o + 1
    node_4.next = node_5
    o = o + 1
    node_5.next = node_6
    o = o + 1
    node_6.next = node_7
    o = o + 1
    node_7.next = node_8
    o = o + 1
    node_8.next = node_9
    o = o + 1
    node_9.next = node_10

    func_calls(o, o_ll, o_la, o_bin)

if __name__ == "__main__":
    main(1, 7, 4, 2, 9, 8, 10, -4, 0, 3)
    
# pytest
# def test_main(capsys):
#     main(1, 7, 4, 2, 9, 8, 10, -4, 0, 3)
#     captured = capsys.readouterr()
#     assert ("8") in captured.out

# # pytest
# def test_reg(capsys):
#     main(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     captured = capsys.readouterr()
#     assert ("8") in captured.out

# # pytest
# def test_rev(capsys):
#     main(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#     captured = capsys.readouterr()
#     assert ("8") in captured.out


"""
Design: I initially went off the lessons provided in the class so far.
Develope: I rewrote the lessons to meet the needs of the assignment, but getting the arguments passed into main to populate the linked list was a challenge. 
Test: I tested the program with the required arguments, along with 1-9 and the reverse.
Documentation:
The above program finds 8 from the numbers passed to main. It first performs a linear search on the linked list, then creates an array from the linked list, 
then performs a linear search on the array, and finally performs a binary search on the sorted array. The program is tested with pytest. 
"""