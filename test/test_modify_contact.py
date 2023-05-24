# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact_py(app):
    new_fname="Sergey"
    contact = Contact(firstname=new_fname, middlename="Semenovich", lastname="Ivanov")
    if not app.contact.exists("Ivanov"):
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = 0
    for element in old_contacts:
        if element.lastname == "Ivanov":
            old_contacts[index].firstname = new_fname
            break
        else:
            index = index + 1
    app.contact.modify("Ivanov", contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact(app):
    new_fname = "Sergey"
    contact = Contact(firstname=new_fname, middlename="Semenovich", lastname="Ivanov")
    if not app.contact.exists("Ivanov"):
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    rand_index_max = 0
    # из чего будем выбирать (после фильтрации)
    for element in old_contacts:
        if element.lastname == "Ivanov":
            rand_index_max = rand_index_max + 1
    rand_index = randrange(rand_index_max)
    # что менять в исходном списке, для сравнения
    index = 0
    temp_index = 0
    for element in old_contacts:
        if element.lastname == "Ivanov":
            if temp_index == rand_index:
                old_contacts[index].firstname = new_fname
                break
            temp_index = temp_index + 1
        index = index + 1

    app.contact.modify_by_index("Ivanov", contact, rand_index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



