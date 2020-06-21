# Huffman Coding with Heap Tree BFS

## Requirements
To generate unique binary code for each character of string message by providing `huffman_encode()` and `huffman_decode()` methods.

- Huffman code = prefix code, where the `whole code` for any character is `not a prefix` of any other code. 
- Huffman binary code is shorter for the more frequent character, and vice-versa.
- Huffman code requires a much lesser amount of memory in binary form as compared to the entire string message.

## Design Principle
- Tree is chosen to structure and generate Huffman binary code.
- Heapq is chosen to track and pop Tree node with lowest frequency in `O(1)` time.
- Deque `doubly ended queue` is chosen to perform `Tree BFS (breadth first search)` traversal.

### huffman_encoding():
- n = `num of leaf_node` (num_character_types)
- Time complexity: `O(n)`
- Space complexity: `O(n)`

### huffman_decoding():
- m = `len of encoded_digits`
- n = `num of leaf_node` (num_character_types)
- Time complexity: `O(m)`
- Space complexity: `O(m+n)`
