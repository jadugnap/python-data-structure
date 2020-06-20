from find_files import find_files

# use either option below
# 1. use this to run `pytest` from repo home directory
prefix = 'problem2_Recursion/'
# 2. use this to run pytest from problem2 subdirectory
# prefix = ''

def test_py_testdir():
    files_found = find_files(prefix+"py_testdir", ".py", False)
    answers = [prefix+"py_testdir/folder1/folder12/file12.py", prefix+"py_testdir/folder1/folder11/file11.py", prefix+"find_files.py"]
    assert(len(files_found)>0)
    for i,filename in enumerate(files_found):
        assert(filename==answers[i])

def test_c_testdir():
    files_found = find_files(prefix+"c_testdir", ".c", False)
    answers = [prefix+"c_testdir/subdir3/subsubdir1/b.c", prefix+"c_testdir/t1.c", prefix+"c_testdir/subdir5/a.c", prefix+"c_testdir/subdir1/a.c"]
    assert(len(files_found)>0)
    for i,filename in enumerate(files_found):
        assert(filename==answers[i])

def test_nonmatching_suffix():
    files_found = find_files(prefix+"py_testdir", ".404notfound", False)
    answers = [prefix+"py_testdir/folder1/file1.notpy"]
    assert(len(files_found)==0)
    assert(files_found==[])
