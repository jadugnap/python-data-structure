# Find Files with Recursion

## Requirements
To write method for finding all files under a directory (and all subdirectories beneath it) ending with specified `.suffix`.

- Python's `os.walk()` method is not allowed to use.
- `os.path.isdir()` may be used.
- `os.path.isfile()` may be used.
- `os.listdir()` may be used.
- `os.path.join()` may be used.

## Design Principle
- Recursion is chosen to walk through each layer of subdirectories.

### find_files():
- m = `depth`
- n = `num_files in directory_layer`
- Time complexity: `O(m * n)`
- Space complexity: `O(m)`
