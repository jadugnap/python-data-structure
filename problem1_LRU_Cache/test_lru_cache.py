from lru_cache import LRU_Cache

def test_lru_cache():
    our_cache = LRU_Cache(5, is_debug=True)
    our_cache.set(1, 11)
    our_cache.set(2, 12)
    our_cache.set(3, 13)
    our_cache.set(4, 14)

    assert(our_cache.get(2)==12)
    # returns 12

    our_cache.set(4, 404)

    assert(our_cache.get(1)==11)
    # returns 11

    assert(our_cache.get(9)==-1)
    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 15) 
    our_cache.set(6, 16)

    assert(our_cache.get(3)==-1)
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
