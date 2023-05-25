
def test_email_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails == merge_emails_like_home_page(contact_from_edit_page)

def test_address_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_emails == merge_emails_like_home_page(contact_from_edit_page)

def merge_emails_like_home_page(contact):
    result = "\n".join(filter(lambda x : x != "",filter(lambda x : x is not None,
                                                               [contact.email, contact.email2, contact.email3]
                                     )
                              )
              )
    if result is None:
          result=""
    return result