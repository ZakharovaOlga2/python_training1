# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group_py(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group("21212", "vsdvsdvsd", "ebrbsf d"))
    app.session.logout()

def test_add_empty_group_py(app):
    app.session.login( login="admin", password="secret")
    app.group.create(Group("", "", ""))
    app.session.logout()


