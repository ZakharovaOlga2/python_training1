# -*- coding: utf-8 -*-

def test_delete_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


