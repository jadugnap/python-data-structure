# User Group with DFS Recursion

## Requirements
To provide an efficient look up of whether the user is a member of the specified group.

## Design Principle
- Recursion is chosen to perform `Tree DFS (depth first search)` traversal.

### is_user_in_group():
- m = `depth`
- n = `num_users in group`
- Time complexity: `O(m * n)`
- Space complexity: `O(m * n)`
