from user_group import *

def prepare_testcases_user_group():
    # create test_cases map
    tc = {}

    tc["parent"] = Group("parent")
    tc["child"] = Group("child")
    tc["grand_child"] = Group("grand_child")
    tc["gg_child"] = Group("gg_child")
    tc["uncle"] = Group("uncle")
    tc["cousin"] = Group("cousin")

    tc["gg_child"].add_user("gg_child_user")
    tc["grand_child"].add_user("grand_child_user")
    tc["child"].add_user("child_user")
    tc["cousin"].add_user("cousin_user")

    tc["grand_child"].add_group(tc["gg_child"])
    tc["child"].add_group(tc["grand_child"])
    tc["parent"].add_group(tc["child"])
    tc["uncle"].add_group(tc["cousin"])

    return tc

def test_greatgrand_child_user():
    tc = prepare_testcases_user_group()
    assert(is_user_in_group("gg_child_user", tc["parent"])==True)
    assert(is_user_in_group("gg_child_user", tc["child"])==True)
    assert(is_user_in_group("gg_child_user", tc["grand_child"])==True)
    assert(is_user_in_group("gg_child_user", tc["gg_child"])==True)
    assert(is_user_in_group("gg_child_user", tc["cousin"])==False)
    assert(is_user_in_group("gg_child_user", tc["uncle"])==False)

def test_grand_child_user():
    tc = prepare_testcases_user_group()
    assert(is_user_in_group("grand_child_user", tc["parent"])==True)
    assert(is_user_in_group("grand_child_user", tc["child"])==True)
    assert(is_user_in_group("grand_child_user", tc["grand_child"])==True)
    assert(is_user_in_group("grand_child_user", tc["gg_child"])==False)

def test_child_user():
    tc = prepare_testcases_user_group()
    assert(is_user_in_group("child_user", tc["parent"])==True)
    assert(is_user_in_group("child_user", tc["child"])==True)
    assert(is_user_in_group("child_user", tc["grand_child"])==False)
    assert(is_user_in_group("child_user", tc["gg_child"])==False)

def test_cousin_user():
    tc = prepare_testcases_user_group()
    assert(is_user_in_group("cousin_user", tc["cousin"])==True)
    assert(is_user_in_group("cousin_user", tc["uncle"])==True)
    assert(is_user_in_group("cousin_user", tc["parent"])==False)
    assert(is_user_in_group("cousin_user", tc["gg_child"])==False)

def test_subgroup_in_group():
    tc = prepare_testcases_user_group()
    assert(is_user_in_group("gg_child", tc["gg_child"])==True)
    assert(is_user_in_group("gg_child", tc["grand_child"])==True)
    assert(is_user_in_group("gg_child", tc["parent"])==True)
    assert(is_user_in_group("gg_child", tc["uncle"])==False)
    assert(is_user_in_group("grand_child", tc["gg_child"])==False)
    assert(is_user_in_group("grand_child", tc["grand_child"])==True)
    assert(is_user_in_group("grand_child", tc["parent"])==True)
    assert(is_user_in_group("grand_child", tc["uncle"])==False)
    assert(is_user_in_group("cousin", tc["uncle"])==True)
    assert(is_user_in_group("cousin", tc["cousin"])==True)
    assert(is_user_in_group("cousin", tc["parent"])==False)
