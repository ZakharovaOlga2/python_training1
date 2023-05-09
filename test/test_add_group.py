# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group_py(app):
    app.group.create(Group("21212", "vsdvsdvsd", "ebrbsf d"))

def test_add_empty_group_py(app):
    app.group.create(Group("", "", ""))
