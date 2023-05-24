# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_py(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Фролович", lastname="Petrov", nickname="Vano", title="Petrov Ivan", company="ISU", address="Москва" ,home="Питер", mobile="900000000", work="isu", email="a@a.ru", email2="a@a.ru", homepage="ISU.ru", bday="16", bmonth="September", byear="1980")
    app.contact.create(contact)
    new_contacts  = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)