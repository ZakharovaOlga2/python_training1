# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact_py(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nfirstnameame="Для удаления"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    # если приложение старое, то удаление не происходит и проверка падает
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts






