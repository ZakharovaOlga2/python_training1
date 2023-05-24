# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    old_id = "2"
    new_id = "1"
    if not app.group.exists(old_id):
        app.group.create(Group(old_id, "Folk", "Volk"))
    old_groups = app.group.get_group_list()
    group = Group(new_id, "abcde", "edcba")
    index = 0
    for element in old_groups:
        if element.name==old_id:
            old_groups[index].name = new_id
            break
        else:
            index = index + 1
    app.group.modify(old_id, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
