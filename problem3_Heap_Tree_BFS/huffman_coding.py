import sys, copy
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
        # BFS tree traversal
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
            # huffman_code[left] = '0'
            if node.has_left_child():
                q.enq( (node.get_left_child(), level+1, code+'0') )
            else:
                q.enq( (None, level+1, '') )
            # huffman_code[right] = '1'
            if node.has_right_child():
                q.enq( (node.get_right_child(), level+1, code+'1') )
            else:
                q.enq( (None, level+1, '') )
        s = "Tree\n"
        previous_level = -1
        # combine huffman_code[left] and huffman_code[right]
        huffman_code = {}
        for i in range(len(visit_order)):
            node, level, code = visit_order[i]
            if node and len(node.get_name())==1:
                huffman_code[node.get_name()] = code
        return huffman_code

    def hardcode_single_huffman_code(self):
        # Set a tree where right_node = (deepcopy of) root_node = this single character
        root_node = self.get_root()
        right_node = copy.deepcopy(root_node)
        root_node.set_right_child(right_node)
        # hardcode the huffman_code[letter] = '1'
        return {right_node.get_name(): '1'}

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
    # Encode each character by huffman_tree with unique prefix binary code
    # for an empty character (edge case)
    if len(msg)==0:
        return '', None
    heap_of_tree = set_frequency_map(msg)
    # for a single character type (edge case)
    if len(heap_of_tree) == 1:
        if is_debug: print(f"heap_of_tree = {heap_of_tree}")
        huffman_tree = heap_of_tree[0]
        huffman_code = huffman_tree.hardcode_single_huffman_code()
    # for multiple character types
    else:
        while len(heap_of_tree) > 1:
            if is_debug: print(f"heap_of_tree = {heap_of_tree}")
            heap_of_tree = pop_minimum_pair(heap_of_tree)
        if is_debug: print(f"final heap_of_tree = {heap_of_tree}")
        huffman_tree = heap_of_tree[0]
        huffman_code = huffman_tree.traverse_huffman_code()
    if is_debug: print(f"huffman_code: {huffman_code}")
    encoded_msg = ''
    for letter in msg:
        encoded_msg += huffman_code[letter]
    return encoded_msg, huffman_tree

def huffman_decoding(msg,tree):
    # Decode binary codes back into string message with huffman_tree
    if tree == None:
        # for an empty character (edge case)
        return ''
    node = tree.get_root()
    decoded_msg = ''
    for digit in msg:
        # digit '0' -> visit left_child
        if digit == '0':
            node = node.get_left_child()
        # digit '1' -> visit right_child
        elif digit == '1':
            node = node.get_right_child()
        # is_leaf node -> decode letter & restart from root_node
        if node.is_leaf():
            decoded_msg += node.get_name()
            node = tree.get_root()
    return decoded_msg

if __name__ == "__main__":
    msg_list = []
    msg_list += ["the quick brown fox jumps over a lazy dog"]
    msg_list += ["abcdeabcdabcaba"]
    msg_list += ["www"]
    msg_list += ["x"]
    msg_list += [""]

    for msg in msg_list:
        print("The size of the data is: {}".format(sys.getsizeof(msg)))
        print("The content of the data is: {}\n".format(msg))

        # set is_debug=True to print the debug output walkthrough
        encoded_msg, tree = huffman_encoding(msg, is_debug=True)
        # # leave it blank to print the normal output
        # encoded_msg, tree = huffman_encoding(msg)
        if len(encoded_msg)>0:
            print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_msg, base=2))))
            print("The content of the encoded data is: {}\n".format(encoded_msg))
        # for an empty character (edge case)
        else:
            print("The content of the encoded data is: '' (empty string)\n")

        decoded_msg = huffman_decoding(encoded_msg, tree)
        print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_msg)))
        print("The content of the encoded data is: {}\n".format(decoded_msg))
        print("==================================================\n")
