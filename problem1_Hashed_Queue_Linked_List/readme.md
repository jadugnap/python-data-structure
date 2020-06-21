# LRU Cache with Hashed Queue Linked List

## Requirements
To design a `Least Recently Used (LRU) cache` in which we remove the `least recently used` entry when the cache reaches its limit, by providing both `get()` and `set()` methods.

- In case of a `cache hit`, `get()` method should return its corresponding value.
- In case of a `cache miss`, `get()` method should return -1.
- While putting an element in the cache, `set()` method should insert the element.
- If the cache is full, it should remove the `least recently used` entry first (either `get` or `set`) and then insert the element.
- All operations must take O(1) time.

## Design Principle
- Queue with Linked-List is chosen for setting & getting Cache and tracking cache keys from the `least` to the `most` recently used.
- Hash map (Python's `dictionary`) is chosen to map `Cache[key] = Node(key,value)` in the Queue to achieve `O(1)` time.

### LRU_Cache:
- Space complexity: `O(n)` for `n = capacity`

### LRU_Cache.get():
- Time complexity: `O(1)`

### LRU_Cache.set():
- Time complexity: `O(1)`
