# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact_py(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()






