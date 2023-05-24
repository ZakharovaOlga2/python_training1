# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

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


def test_modify_some_group(app):
    old_id = "2"
    new_id = "1"
    if not app.group.exists(old_id):
        app.group.create(Group(old_id, "Folk", "Volk"))
    group = Group(new_id, "abcde", "edcba")
    old_groups = app.group.get_group_list()
    # из чего будем выбирать (после фильтрации)
    rand_index_max = 0
    for element in old_groups:
        if element.name ==old_id:
            rand_index_max = rand_index_max +1
    rand_index = randrange(rand_index_max)
    # что менять в исходном списке, для сравнения
    index = 0
    temp_index = 0
    for element in old_groups:
        if element.name ==old_id:
            if temp_index == rand_index:
                old_groups[index].name = new_id
                break
            temp_index = temp_index + 1
        index = index + 1
    app.group.modify_group_by_index(old_id, group, rand_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)