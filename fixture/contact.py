from selenium.webdriver.common.keys import Keys

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def type_contract_dropdown(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).send_keys(value)

    def type_contract_property(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def create(self, contact):
        wd = self.app.wd
        self.header_menu_navigation("add new")
        # init first name
        self.type_contract_property("firstname", contact.firstname)
        self.type_contract_property("middlename", contact.middlename)
        self.type_contract_property("lastname", contact.lastname)
        self.type_contract_property("nickname", contact.nickname)
        self.type_contract_property("title", contact.title)
        self.type_contract_property("company", contact.company)
        self.type_contract_property("address", contact.address)
        self.type_contract_property("home", contact.home)
        self.type_contract_property("mobile", contact.mobile)
        self.type_contract_property("work", contact.work)
        self.type_contract_property("email", contact.email)
        self.type_contract_property("email2", contact.email2)
        self.type_contract_property("homepage", contact.homepage)
        self.type_contract_dropdown("bday", contact.bday)
        self.type_contract_dropdown("bmonth", contact.bmonth)
        self.type_contract_property("byear", contact.byear)
        # save form
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()

    def exists(self, search_filter):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # filter
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys(search_filter)
        # count visible filtered values
        cnt_all = len(wd.find_elements_by_xpath("//img[@title='Edit']"))
        cnt_invisible = len(wd.find_elements_by_xpath("//tr[contains(@style,'display: none')]//img[@title='Edit']"))
        cnt_visible = cnt_all - cnt_invisible
        # clear filter to next works
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").clear()
        wd.find_element_by_name("searchstring").send_keys(Keys.RETURN)
        if cnt_visible > 0:
            return True
        return False


    def modify(self, search_filter, contact):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # filter
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys(search_filter)
        # edit instance or exit (if there are no results)
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # init first name
        self.type_contract_property("firstname", contact.firstname)
        self.type_contract_property("middlename", contact.middlename)
        self.type_contract_property("lastname", contact.lastname)
        # save form
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # return
        alert = wd.switch_to_alert()
        alert.accept()

    def header_menu_navigation(self, item):
        wd = self.app.wd
        wd.find_element_by_link_text(item).click()

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def count(self):
        wd = self.app.wd
        self.header_menu_navigation("home")
        return len(wd.find_elements_by_name("selected[]"))

