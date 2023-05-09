# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_py(app):
    app.contact.create(Contact(firstname="Ivan", middlename="Фролович", lastname="Petrov", nickname="Vano", title="Petrov Ivan", company="ISU", address="Москва" ,home="Питер", mobile="900000000", work="isu", email="a@a.ru", email2="a@a.ru", homepage="ISU.ru", bday="16", bmonth="September", byear="1980"))
