from union_intersection import *

def test_ui_list():
    list1 = LinkedList()
    list2 = LinkedList()
    element1 = [3,2,4,35,6,65,6,4,3,21]
    element2 = [6,32,4,9,6,1,11,21,1]
    for i in element1:
        list1.append_node(i)
    for i in element2:
        list2.append_node(i)

    s1 = set(element1)
    s2 = set(element2)
    assert(union_func(list1,list2).get_size()==len(s1.union(s2)))
    assert(intersection_func(list1,list2).get_size()==len(s1.intersection(s2)))

def test_ui_duplicate():    
    list1 = LinkedList()
    list2 = LinkedList()
    element1 = [4,4]
    element2 = [4,4]
    for i in element1:
        list1.append_node(i)
    for i in element2:
        list2.append_node(i)

    assert(union_func(list1,list2).get_size()==1)
    assert(union_func(list1,list2).get_head().get_value()==4)
    assert(intersection_func(list1,list2).get_size()==1)
    assert(intersection_func(list1,list2).get_head().get_value()==4)

def test_ui_no_intersection():    
    list1 = LinkedList()
    list2 = LinkedList()
    element1 = [404,303]
    element2 = [202,101]
    for i in element1:
        list1.append_node(i)
    for i in element2:
        list2.append_node(i)

    assert(union_func(list1,list2).get_size()==4)
    assert(intersection_func(list1,list2).get_size()==0)
    assert(intersection_func(list1,list2).get_head()==None)
