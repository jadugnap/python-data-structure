import os

def is_terminal(path_lists):
    return path_lists == []

def is_directory(joined_path):
    return os.path.isdir(joined_path)

def is_matching_suffix(joined_path, suffix):
    return joined_path.endswith(suffix)

def get_path_lists(fullpath, debug, spacing):
    path_lists = os.listdir(fullpath)
    if debug:
        print(f"{spacing}Directory ({fullpath})'s path_lists = {path_lists}")
    return path_lists

def handle_base_case(fullpath, debug, spacing):
    if debug:
        print(f"{spacing}No file inside '{fullpath}', wrap up")
    return []

def handle_recursive_dir(joined_path, suffix, debug, spacing, index):
    if debug:
        print(f"{spacing}({index}) `{joined_path}` is a directory, drill down")
    return find_files(joined_path, suffix, debug, spacing+'    ')

def handle_match_suffix(joined_path, suffix, debug, spacing, index):
    if debug:
        print(f"{spacing}({index}) `{joined_path}` ends with `{suffix}`, add into 'files_found`")
    return [joined_path]

def handle_mismatch_suffix(joined_path, suffix, debug, spacing, index):
    if debug:
        print(f"{spacing}({index}) `{joined_path}` does not end with `{suffix}`, wrap up")

def find_files(fullpath, suffix, debug=False, spacing=''):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      path(str): path of the file system
      suffix(str): suffix if the file name to be found
      debug(bool): boolean switch for printing debug info, default is False
      spacing(str): recursive call indentation for debug info, default is empty string

    Returns:
       a list of paths
    """
    path_lists = get_path_lists(fullpath, debug, spacing)
    if is_terminal(path_lists):
        return handle_base_case(fullpath, debug, spacing)
    files_found = []
    for index,new_path in enumerate(path_lists):
        joined_path = os.path.join(fullpath, new_path)
        if is_directory(joined_path):
            files_found += handle_recursive_dir(joined_path, suffix, debug, spacing, index)
        elif is_matching_suffix(joined_path, suffix):
            files_found += handle_match_suffix(joined_path, suffix, debug, spacing, index)
        else:
            handle_mismatch_suffix(joined_path, suffix, debug, spacing, index)
    return files_found
