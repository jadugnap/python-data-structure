class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        new_list = []
        pointer = self.head
        while pointer != None:
            new_list.append(str(pointer.key))
            pointer = pointer.next
        return ','.join(new_list)

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            old_tail = self.tail
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
            self.tail.prev = old_tail    # add tail.prev directed to the old tail
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head                 # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.head.prev = None            # remove head.prev
        self.length -= 1
        return node

    def remove(self, node):
        if node == None:
            return
        old_prev = node.prev
        old_next = node.next
        if self.is_head(node):
            self.head = old_next
        else:
            node.prev.next = old_next
        if self.is_tail(node):
            self.tail = old_prev
        else:
            node.next.prev = old_prev
        self.length -= 1

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def is_head(self, node):
        return node.prev == None

    def is_tail(self, node):
        return node.next == None

class LRU_Cache(object):
    def __init__(self, capacity, is_debug):
        # Initialize class variables
        self.capacity = capacity
        self.queue = Queue()
        self.hashmaps = {}
        self.is_debug = is_debug

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.hashmaps.get(key, None)
        if node == None:
            print(f"missing Cache[{key}] = -1")
            return -1
        # key is most recently used
        self.arrange_mru(node.key, node.value, node, "hitting")
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # if cache hit -> arrange_mru() & return early
        node = self.hashmaps.get(key, None)
        if node != None:
            # key is most recently used
            self.arrange_mru(node.key, node.value, node, "updating")
            return
        # queue hits capacity -> arrange_lru()
        if self.queue.size() >= self.capacity:
            if self.is_debug: print(f"inserting Cache[{key}] = {value} into a full queue = {self.queue}")
            self.arrange_lru(key, value)
        # now as queue fits capacity -> arrange_mru()
        self.arrange_mru(key, value, None, "storing")

    def arrange_mru(self, key, value, node, action):
        # Arrange the Most Recently Used cache to the end of queue
        self.queue.remove(node)
        self.queue.enqueue(key, value)
        self.hashmaps[key] = self.queue.tail
        print(f"{action} Cache[{key}] = {value}")
        if self.is_debug: print(f"current queue = {self.queue}\n")

    def arrange_lru(self, key, value):
        # Pop the Least Recently Used cache from the beginning of queue
        node = self.queue.dequeue()
        self.hashmaps.pop(node.key, None)
        if self.is_debug: print(f"deleting LRU Cache[{node.key}] = {node.value}")
