# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_del_contact_py(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Для удаления"))
    old_contacts = db.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = db.get_contact_list()
    # если приложение старое, то удаление не происходит и проверка падает
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert new_contacts == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Для удаления"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    # если приложение старое, то удаление не происходит и проверка падает
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert new_contacts == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)





