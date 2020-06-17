from find_files import find_files

def test_py_testdir():
    files_found = find_files("py_testdir", ".py", False)
    answers = ["py_testdir/folder1/folder12/file12.py", "py_testdir/folder1/folder11/file11.py", "./find_files.py"]
    for i,filename in enumerate(files_found):
        assert(filename==answers[i])

def test_c_testdir():
    files_found = find_files("c_testdir", ".c", False)
    answers = ["c_testdir/subdir3/subsubdir1/b.c", "c_testdir/t1.c", "c_testdir/subdir5/a.c", "c_testdir/subdir1/a.c"]
    for i,filename in enumerate(files_found):
        assert(filename==answers[i])
