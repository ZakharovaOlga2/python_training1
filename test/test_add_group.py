# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_py(app):
    old_groups = app.group.get_group_list()
    group = Group("21212", "vsdvsdvsd", "ebrbsf d")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group_py(app):
    old_groups = app.group.get_group_list()
    group = Group("", "", "")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
