class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user (or subgroup) is in the group, False otherwise.
    Implement recursive DFS into non-binary tree (may have > 2 child nodes).

    Args:
      user(str): user name / subgroup name
      group(class:Group): group to check user membership against
    """
    # base case
    if user == group.get_name() or user in group.get_users():
        return True
    # recursive case
    for subgroup in group.get_groups():
        return is_user_in_group(user, subgroup)
    # after all other cases mismatch
    return False
