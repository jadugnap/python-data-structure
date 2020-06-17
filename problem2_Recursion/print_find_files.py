from find_files import find_files

if __name__ == "__main__":
    print("normal mode results:")
    files_found = find_files("c_testdir", ".c", False)
    for filename in files_found:
        print(filename)

    print("\ndebug mode:")
    files_found = find_files("c_testdir", ".c", True)
    print("results:")
    for filename in files_found:
        print(filename)
