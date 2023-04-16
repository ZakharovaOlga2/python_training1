# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group_py(app):
    app.login(login="admin", password="secret")
    app.add_new_group(Group("21212", "vsdvsdvsd", "ebrbsf d"))
    app.logout()

def test_add_empty_group_py(app):
    app.login( login="admin", password="secret")
    app.add_new_group(Group("", "", ""))
    app.logout()


