# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phones(minlen,maxlen):
    symbols = string.digits+"()+-"
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen,maxlen))])

testdata = [
    Contact(firstname=firstname, lastname=lastname, middlename=middlename,  mobile=mobile)
    for firstname in [random_string("F",25)]
    for lastname in [random_string("L",25)]
    for middlename in ["",random_string("M",25)]
    for mobile in ["",random_phones(10,14)]
]
@pytest.mark.parametrize("contact",testdata,ids=[repr(x) for  x in testdata])
def test_add_contact_py(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(Contact(firstname=contact.firstname,lastname=contact.lastname))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)