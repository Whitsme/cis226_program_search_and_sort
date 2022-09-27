import pytest
import nodes_included

array = []
nodes = []
links = []

def main(array):
    if array == []:
        nodes_included.main()
    if node_gen(array):
        pass
    print('Starting linear search on linked list...')
    lin_search_llist(nodes[0], find=8)
    print('Starting linear search on array...')
    if trav_dl_list(nodes[0]):
        if lin_search_array(array, 8):
            print ('Starting binary search on sorted array...')
    bin_search(array, 8)
    
def lin_search_llist(node, find, traversed=None):
    traversed = traversed or []
    if not node or node in traversed:
        return
    traversed.append(node)
    if node.prev:
        lin_search_llist(node.prev, find, traversed=traversed)
    if int(node.data) == find:
        print (node.data)
        return True  
    if node.next:
        lin_search_llist(node.next, find, traversed=traversed)

def lin_search_array(array, find):
    for i, value in enumerate(array):
        if int(value) == find:
            print (value)
    return True

def bin_search(array, find):
    s_sort(array)
    begin = 0
    end = len(array) - 1
    find = 8
    while find <= 0 and begin <= end:
        mid = int((begin + end) / 2)
        if array[mid] == find:
            find = mid
        elif array[mid] < find:
            begin = mid + 1
        else:
            end = mid - 1
    print(find)

def swapper(array, index1, index2):
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp

def s_sort(array):
    for marker_c in range(len(array) - 1):
        marker_a = marker_c
        for marker_b in range(marker_c, len(array)):
            if array[marker_b] < array[marker_c]:
                marker_c = marker_b
        if marker_c != marker_a:
            swapper(array, marker_c, marker_a)
    return array

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev 
        self.next = next 
    
    # def __reper__(self, data):
    #     if self.start_node is None:
    #         new_node = Node(data)
    #         self.start_node = new_node
    #         print("node inserted")
    #         return
    #     new_node = Node(data)
    #     new_node.nref = self.start_node
    #     self.start_node.pref = new_node
    #     self.start_node = new_node

def trav_dl_list(node, traversed=None):
    traversed = traversed or []
    if not node or node in traversed:
        return
    traversed.append(node)
    if node.prev:
        trav_dl_list(node.prev, traversed=traversed)

    array.append(node.data)
    if node.next:
        trav_dl_list(node.next, traversed=traversed)
    return True

def node_gen(input):
    """Generator that yields nodes"""
    try: 
        i = 1
        for num in input:
            try:
                num = int(num)
                node = ("node_%s" % i)
                node = node.replace(" ", "")
                link = ("%s.next" % node)
                link = link.replace(" ", "")   
                next_node = ("node_%s" % (i+1))
                next_node = next_node.replace(" ", "")
                if i == 1:
                    nodes.append(f"{node} = Node('{num}')")
                elif i > 1:
                    prev_node = ("node_%s" % (i-1))
                    prev_node = prev_node.replace(" ", "")
                    nodes.append(f"{node} = Node('{num}', prev={prev_node})")
                links.append(f"{link} = {next_node}")
                i += 1
            except:
                pass
        del links[-1]
    except:
        print("Error: Please enter a valid input containing numbers")
        quit()
    for node in nodes:
        Node.insert_at_start(node)
    return True



if __name__ == "__main__":
    main(array)

def test_main(capsys):
    main(1, 3, 3, 5, 5, 7, 7, 9, 9)
    captured = capsys.readouterr()
    assert (8) in captured.out


