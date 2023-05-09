# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact_py(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nfirstnameame="Для удаления"))
    app.contact.delete_first_contact()






