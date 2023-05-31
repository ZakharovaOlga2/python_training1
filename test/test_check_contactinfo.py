import re
from model.contact import Contact

def tests_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails == merge_emails_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_emails == merge_emails_like_home_page(contact_from_edit_page)
    assert contact_from_view_page.full_name == get_full_name(contact_from_edit_page)
    assert merge_phones_like_home_page(contact_from_view_page) == merge_phones_like_home_page(contact_from_edit_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    if contact_from_edit_page.address != "":
        assert app.contact.get_fullinfo_from_view_page(0).find(contact_from_edit_page.address) > 0



def test_check_all_view_contacts_with_db(app, db):
    db_contacts = db.get_contact_list()
    view_contacts = app.contact.get_contact_list()
    compare_contact_list_info(sorted(db_contacts,key=Contact.id_or_max),sorted(view_contacts,key=Contact.id_or_max))

def compare_contact_list_info(list1,list2):
    error = ""
    if len(list1) != len(list2):
        assert False, "Не совпадает количество контактов в БД и из интерфейса"
    counter = 0
    for contact_list1 in list1:
        contact_list2 = list2[counter]
        if contact_list1.all_emails == contact_list2.all_emails and contact_list1.firstname == contact_list2.firstname and contact_list1.lastname == contact_list2.lastname and contact_list1.all_phones_from_home_page == contact_list2.all_phones_from_home_page and contact_list1.all_emails == contact_list2.all_emails and contact_list2.address == contact_list1.address:
            pass
        else:
            error = error+"\nНе совпадают данные в элементе %s " % counter
        counter = counter + 1
    if error !="":
        assert False, error

def get_full_name(contact):
    result = " ".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                       [contact.firstname, contact.middlename, contact.lastname]))
                      )
    if result is None:
        result = ""
    return result


def merge_emails_like_home_page(contact):
    result = "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                        [contact.email, contact.email2, contact.email3]
                                                        )
                              )
                       )
    if result is None:
        result = ""
    return result


def merge_phones_like_home_page(contact):
    result = "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                     filter(lambda x: x is not None,
                                                            [contact.home, contact.mobile, contact.work,
                                                             contact.phone2])
                                                     )
                              )
                       )
    if result is None:
        result = ""
    return result


def clear(s):
    return re.sub("[() -+]", "", s)

