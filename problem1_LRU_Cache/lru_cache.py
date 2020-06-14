class LRU_Cache(object):
    def __init__(self, capacity, is_debug):
        # Initialize class variables
        self.capacity = capacity
        self.is_debug = is_debug
        self.queue_of_keys = []
        self.queue_length = 0
        self.hashmaps = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self.hashmaps.get(key, -1)
        if value == -1:
            print(f"missing Cache[{key}] = {value}\n")
        else:
            self.arrange_mru(key, value, "hitting")
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        # if cache hit -> arrange_mru() & return early
        if self.hashmaps.get(key, -1) != -1:
            self.arrange_mru(key, value, "updating")
            return
        
        # queue hits capacity -> arrange_lru()
        if self.queue_length >= self.capacity:
            self.arrange_lru(key, value)
        else:
            self.queue_length += 1
        # now as queue fits capacity -> arrange_mru()
        self.arrange_mru(key, value, "storing")

    def arrange_mru(self, key, value, action):
        # Arrange the Most Recently Used cache to the end of queue
        if key in self.queue_of_keys:
            self.queue_of_keys.remove(key)
        self.queue_of_keys.append(key)
        self.hashmaps[key] = value
        print(f"{action} Cache[{key}] = {value}")
        if self.is_debug: print(f"current queue_of_keys = {self.queue_of_keys}\n")

    def arrange_lru(self, key, value):
        # Pop the Least Recently Used cache from the beginning of queue
        if self.is_debug: print(f"inserting Cache[{key}] = {value} into a full queue = {self.queue_of_keys}")
        deleted_key = self.queue_of_keys.pop(0)
        deleted_val = self.hashmaps.pop(deleted_key, None)
        if self.is_debug: print(f"deleting LRU Cache[{deleted_key}] = {deleted_val}")
