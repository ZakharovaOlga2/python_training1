# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_py(app):
    app.contact.modify("Ivanov", Contact(firstname="Petr", middlename="Semenovich", lastname="Ivanov", nickname="", title="", company="", address="", home="", mobile="", work="", email="", email2="", homepage="", bday="", bmonth="", byear=""))






