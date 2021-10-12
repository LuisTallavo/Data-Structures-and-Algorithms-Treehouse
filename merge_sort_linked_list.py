"""
Merge Sort for Linked List Object
"""
from Linked_List import LinkedList

def merge_sort_linked_list(lst):
    if lst.size() == 1 or lst.head == None:
        return lst
    
    left_half, right_half = split(lst)

    left = merge_sort_linked_list(left_half)
    right = merge_sort_linked_list(right_half)

    return merge(left, right)

def split(lst):
    if lst == None or lst.head == None:
        left_half = lst
        right_half = None
        
        return left_half, right_half
    else:
        mid = lst.size()//2
        mid_node = lst.node_at_index(mid - 1)

        left_half = lst
        right_half = LinkedList()
        right_half.head = mid_node.next_node

        mid_node.next_node = None
        return left_half, right_half 


def merge(left, right):
    merged = LinkedList()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head

    #Iterate over left and right until we reach the tail note of either

    while left_head or right_head:
        if left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head == None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node
    head = merged.head.next_node
    merged.head = head
    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort_linked_list(l)
print(sorted_linked_list)

                
    
    
