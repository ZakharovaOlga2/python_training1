# -*- coding: utf-8 -*-
from model.contact import Contact

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






