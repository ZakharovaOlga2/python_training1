# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if not app.group.exists("2"):
        app.group.create(Group("2", "Folk", "Volk"))
    app.group.modify("2", Group("1", "abcde", "edcba"))
