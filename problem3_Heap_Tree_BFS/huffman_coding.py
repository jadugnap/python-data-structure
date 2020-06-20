import sys
from collections import Counter, deque
from heapq import heapify,heappush,heappop

class Node():
    def __init__(self, value=None, name=None):
        self.value = value
        self.name = name
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()

class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

class Tree():
    def __init__(self, value=None, name=None):
        self.root = Node(value, name)
    
    def __repr__(self):
        return f"{self.root.get_value()}" + '-' + self.root.get_name()

    def __lt__(self, other):
        return self.get_root().get_value() < other.get_root().get_value()

    def get_root(self):
        return self.root

    def traverse_huffman_code(self):
        level = 0
        q = Queue()
        visit_order = []
        node = self.get_root()
        q.enq( (node,level,'') )
        while(len(q) > 0):
            node, level, code = q.deq()
            if node == None:
                visit_order.append( (None,level,''))
                continue
            visit_order.append( (node,level,code) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level+1, code+'0') )
            else:
                q.enq( (None, level+1, '') )
            if node.has_right_child():
                q.enq( (node.get_right_child(), level+1, code+'1') )
            else:
                q.enq( (None, level+1, '') )
        s = "Tree\n"
        previous_level = -1
        huffman_code = {}
        for i in range(len(visit_order)):
            node, level, code = visit_order[i]
            if node and len(node.get_name())==1:
                huffman_code[node.get_name()] = code
        return huffman_code

def set_frequency_map(msg):
    # Set a map of frequency of each character in the message
    counts = Counter(msg)
    tree_lists = [Tree(counts[key],key) for key in counts]
    heapify(tree_lists)
    return tree_lists

def pop_minimum_pair(heap):
    # Pop-out two nodes with the minimum frequency
    left_node = heappop(heap).get_root()
    right_node = heappop(heap).get_root()
    new_value = left_node.get_value() + right_node.get_value()
    new_name = f"{left_node.get_name()}{right_node.get_name()}"
    new_tree = Tree(new_value, new_name)
    new_tree.get_root().set_left_child(left_node)
    new_tree.get_root().set_right_child(right_node)
    heappush(heap, new_tree)
    return heap

def huffman_encoding(msg, is_debug=False):
    # Generate unique binary code for each character of our string message
    heap_of_tree = set_frequency_map(msg)
    while len(heap_of_tree) > 1:
        # print(f"heap_of_tree = {heap_of_tree}")
        heap_of_tree = pop_minimum_pair(heap_of_tree)
    # print(f"final heap_of_tree = {heap_of_tree}")
    huffman_tree = heap_of_tree[0]
    huffman_code = huffman_tree.traverse_huffman_code()
    if is_debug:
        print(f"debug: {huffman_code}")
    encoded_msg = ''
    for letter in msg:
        encoded_msg += huffman_code[letter]
    return encoded_msg, huffman_tree

def huffman_decoding(msg,tree):
    node = tree.get_root()
    decoded_msg = ''
    for digit in msg:
        if digit == '0':
            node = node.get_left_child()
        elif digit == '1':
            node = node.get_right_child()
        else:
            print("invalid binary digit")
        if node.is_leaf():
            decoded_msg += node.get_name()
            node = tree.get_root()
    return decoded_msg

if __name__ == "__main__":
    msg_list = []
    msg_list += ["the quick brown fox jumps over a lazy dog"]
    msg_list += ["the five boxing wizards jump quickly"]
    msg_list += ["we promptly judged antique ivory buckles for the next prize"]
    msg_list += ["abcdeabcdabcaba"]

    for msg in msg_list:
        print ("The size of the data is: {}".format(sys.getsizeof(msg)))
        print ("The content of the data is: {}\n".format(msg))

        encoded_msg, tree = huffman_encoding(msg, True)
        # encoded_msg, tree = huffman_encoding(msg)

        print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_msg, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_msg))

        decoded_msg = huffman_decoding(encoded_msg, tree)

        print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_msg)))
        print ("The content of the encoded data is: {}\n".format(decoded_msg))
        print ("==================================================\n")
