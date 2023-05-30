# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_py(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(Contact(firstname=contact.firstname,lastname=contact.lastname))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert new_contacts==sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
