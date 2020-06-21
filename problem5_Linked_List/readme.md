# Blockchain with a Linked List

## Requirements
To link a list of `blocks` into a single `blockchain` with a linked list.

- Each block contains a cryptographic hash of the previous block, a create timestamp, and transaction data.
- Each block in blockchain store information hash with `sha = hashlib.sha256()`.

## Design Principle
- Linked List is chosen to perform `append_block()` in `O(1)` time.

### append_block():
- n = `num_blocks`
- Time complexity: `O(1)`
- Space complexity: `O(n)`
