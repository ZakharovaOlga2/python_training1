# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_py(app):
    if not app.contact.exists("Ivanov"):
        app.contact.create(Contact(firstname="Petr", middlename="Semenovich", lastname="Ivanov"))
    app.contact.modify("Ivanov", Contact(firstname="Petr", middlename="Semenovich", lastname="Ivanov"))






