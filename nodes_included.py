


def main(a, b, c, d, e, f, g, h, i, j):

    array = []

    def func_calls():
        print('Starting linear search on linked list...')
        lin_search_llist(node_1, find=8)
        print('Starting linear search on array...')
        if trav_dl_list(node_1):
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
        quit()

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

    # Create Items
    node_1 = Node(f'{a}')
    node_2 = Node(f'{b}', prev=node_1)
    node_3 = Node(f'{c}', prev=node_2)
    node_4 = Node(f'{d}', prev=node_3)
    node_5 = Node(f'{e}', prev=node_4)
    node_6 = Node(f'{f}', prev=node_5)
    node_7 = Node(f'{g}', prev=node_6)
    node_8 = Node(f'{h}', prev=node_7)
    node_9 = Node(f'{i}', prev=node_8)
    node_10 = Node(f'{j}', prev=node_9)

    # Link up Items
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10

    func_calls()

if __name__ == "__main__":
    main(1, 7, 4, 2, 9, 8, 10, -4, 0, 3)
    