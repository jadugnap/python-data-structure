class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class PriorityQueue:
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
        # set new head to enqueue a very first node
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        # shift the tail, set reference between the old and new tails
        else:
            old_tail = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
            self.tail.prev = old_tail
        self.length += 1

    def dequeue(self):
        # Remove node from 1st position and return it
        # nothing to dequeue when it is empty
        if self.is_empty():
            return None
        # copy the head before modifying it
        node = self.head
        self.length -= 1
        # unset head to dequeue the last remaining node
        if self.is_single_node(node):
            self.head = None
            return node
        # shift the head, unset reference to the old head
        self.head = self.head.next
        self.head.prev = None
        return node

    def remove(self, node):
        # Remove node from any position (not necessarily 1st node)
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

    def is_single_node(self, node):
        return self.is_head(node) and self.is_tail(node)

class LRU_Cache(object):
    def __init__(self, capacity, is_debug):
        """
        Initialize LRU_Cache with specified attributes.

        self.capacity(int): the maximum size of LRU_Cache
        self.queue(class): to track cache key (least -> .. -> most recently used)
        self.hashmaps(dictionary): hashmaps[key] = Node(key,value)
        self.is_debug(boolean) = enable printing debug output
        """
        self.capacity = capacity
        self.queue = PriorityQueue()
        self.hashmaps = {}
        self.is_debug = is_debug

    def get(self, key):
        """
        Return value of specified cache key if it exists.
        Return -1 if key is not present in the cache.

        Args:
        key(int): the cache key to get from cache

        Return:
        value(int): the cache value of the specified key
        """
        node_to_reshuffle = self.hashmaps.get(key, None)
        # cache miss -> key is not present
        if node_to_reshuffle == None:
            if self.is_debug: print(f"missing Cache[{key}] = -1")
            return -1
        # cache hit -> arrange_mru() to reshuffle most recently used key
        self.arrange_mru(key, node_to_reshuffle.value, node_to_reshuffle, "hitting")
        return node_to_reshuffle.value

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache.
        Update the value if the key is existing in the cache.
        If the cache hits capacity, remove the olders key (least recently used).

        Args:
        key(int): the cache key to set into cache
        value(int): the cache value set for the specified key

        Return: None
        """
        if self.capacity <= 0:
            return
        # when cache hits -> arrange_mru() to reshuffle existing key & return early
        node_to_reshuffle = self.hashmaps.get(key, None)
        if node_to_reshuffle != None:
            self.arrange_mru(key, value, node_to_reshuffle, "updating")
            return
        # when capacity hits -> arrange_lru() to provide capacity
        if self.queue.size() >= self.capacity:
            if self.is_debug: print(f"inserting Cache[{key}] = {value} into a full queue = {self.queue}")
            self.arrange_lru()
        # now as capacity fits -> arrange_mru() to store new key
        self.arrange_mru(key, value, None, "storing")

    def arrange_mru(self, key, new_value, node_to_reshuffle, action):
        """
        Arrange the Most Recently Used cache to the end of queue.
        A shared function for storing, updating, and getting the cache.
        Assign hashmaps[key] = Node(key,value) to the tail node.

        Args:
        key(int): the most recently used cache key
        new_value(int): the cache value set for the specified key
        node_to_reshuffle(class:Node): the node carrying key to reshuffle in the PriorityQueue
        action(string): the helper string for debug ("storing", "updating", "hitting")

        Return: None
        """
        self.queue.remove(node_to_reshuffle)
        self.queue.enqueue(key, new_value)
        self.hashmaps[key] = self.queue.tail
        if self.is_debug: print(f"{action} Cache[{key}] = {new_value}")
        if self.is_debug: print(f"current queue = {self.queue}\n")

    def arrange_lru(self):
        """
        Pop the Least Recently Used cache from the beginning of queue.

        Args: None
        Return: None
        """
        node = self.queue.dequeue()
        self.hashmaps.pop(node.key, None)
        if self.is_debug: print(f"deleting LRU Cache[{node.key}] = {node.value}")
