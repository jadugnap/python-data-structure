# Union and Intersection with Two Linked Lists

## Requirements
To take in `two linked lists` and return `a linked list` that is composed of either the `union_func()` or `intersection_func()`, respectively.

- `All elements` from either list should be a member of `union_list`
- `Only matching elements` from both lists should be a member of intersection's `final_list`

## Design Principle
- Store intermediate data in Python's built-in `set()` data type, before transferring from both lists into the final linked list.
- The `set()` data type is chosen to check `if value in set:` with O(1) time.

## union_func():
- n = `num_elements in each list`
- Time complexity: `O(n)`
- Space complexity: `O(n)`

## intersection_func():
- n = `num_elements in each list`
- Time complexity: `O(n)`
- Space complexity: `O(n)`
