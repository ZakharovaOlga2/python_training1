# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.modify("2", Group("1", "abcde", "edcba"))
    app.session.logout()