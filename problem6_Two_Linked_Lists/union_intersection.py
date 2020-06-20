class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        linked_list = str(cur_head.get_data())
        cur_head = cur_head.next
        while cur_head:
            linked_list += " -> " + str(cur_head.get_data())
            cur_head = cur_head.next
        return linked_list

    def append_node(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return self.tail
        node = self.tail
        # node.next = Node(value)
        node.set_next(Node(value))
        self.tail = node.next
        self.size += 1
        return self.tail

    def get_head(self):
        return self.head

    def get_size(self):
        return self.size

def union_func(list1, list2):
    # Take 2 linked lists and return a linked list of its union
    union_set = set()
    # append unique values from list1 into union_set
    head1 = list1.get_head()
    while head1:
        union_set.add(head1.get_value())
        head1 = head1.next
    # append unique values from list2 into union_set
    head2 = list2.get_head()
    while head2:
        union_set.add(head2.get_value())
        head2 = head2.next
    # convert union_set into a linked list and return
    union_list = LinkedList()
    for member in union_set:
        union_list.append_node(member)
    return union_list

def intersection_func(list1, list2):
    # Take 2 linked lists and return a linked list of its intersection
    temp_set = set()
    final_set = set()
    # append unique values from list1 into temp_set
    head1 = list1.get_head()
    while head1:
        value = head1.get_value()
        temp_set.add(value)
        head1 = head1.next
    # append unique values from list2 (WHICH are member of temp_set) into final_set
    head2 = list2.get_head()
    while head2:
        value = head2.get_value()
        if value in temp_set:
            final_set.add(value)
        head2 = head2.next
    # convert final_set into a linked list and return
    final_list = LinkedList()
    for member in final_set:
        final_list.append_node(member)
    return final_list
