

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[3]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(3)
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_address_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    if contact_from_edit_page.address != "":
        assert app.contact.get_fullinfo_from_view_page(0).find(contact_from_edit_page.address)>0



