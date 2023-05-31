import re
import time

from selenium.webdriver.common.keys import Keys
from model.contact import Contact

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
        self.fill_contact_info(contact)
        # save form
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_xpath("//a[text()='home']").click()
        self.contact_cache = None

    def exists(self, search_filter):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # filter
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys(search_filter)
        # count visible filtered values
        cnt_visible = self.count_visible_element(wd)
        # clear filter to next works
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").clear()
        wd.find_element_by_name("searchstring").send_keys(Keys.RETURN)
        if cnt_visible > 0:
            return True
        return False

    def fill_contact_info(self, contact):
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

    def modify(self, search_filter, contact):
        self.modify_by_index(search_filter, contact,0)

    def modify_by_index(self, search_filter, contact,index):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # filter
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys(search_filter)
        # edit instance or exit (if there are no results)
        cnt_visible = self.count_visible_element(wd)
        if cnt_visible > 0:
            wd.find_elements_by_xpath("//tr[not(contains(@style,'display: none'))]//img[@title='Edit']")[index].click()
            self.fill_contact_info(contact)
            wd.find_element_by_name("update").click()
        # save form
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def count_visible_element(self, wd):
        cnt_all = len(wd.find_elements_by_xpath("//img[@title='Edit']"))
        cnt_invisible = len(wd.find_elements_by_xpath("//tr[contains(@style,'display: none')]//img[@title='Edit']"))
        cnt_visible = cnt_all - cnt_invisible
        return cnt_visible

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.header_menu_navigation("home")
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # return
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None

    def header_menu_navigation(self, item):
        wd = self.app.wd
        if item == 'add new':
            if len(wd.find_elements_by_xpath("//input[@type='submit' and @value='Enter']")) > 0:
                return
        if item == 'home':
            if (len(wd.find_elements_by_id("search_count")) > 0):
                return
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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache == None:
            wd = self.app.wd
            self.header_menu_navigation("home")
            self.contact_cache = []
            # wd.find_elements_by_xpath("//tr[not(contains(@style,'display: none')) and @name='entry']"):
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,address=address,all_emails=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.header_menu_navigation("home")
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.header_menu_navigation("home")
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname,id=id,home=home,work=work,mobile=mobile,phone2=phone2,middlename=middlename,address=address,email=email,email2=email2,email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = ""
        if re.search("H: (.*)", text) is not None:
            home = re.search("H: (.*)", text).group(1)
        work = ""
        if re.search("W: (.*)", text) is not None:
            work = re.search("W: (.*)", text).group(1)
        mobile = ""
        if re.search("M: (.*)", text) is not None:
            mobile = re.search("M: (.*)", text).group(1)
        phone2 = ""
        if re.search("P: (.*)", text) is not None:
            phone2 = re.search("P: (.*)", text).group(1)
        full_name = ""
        if len(wd.find_element_by_id("content").find_elements_by_tag_name("b"))>0:
            full_name =  wd.find_element_by_id("content").find_elements_by_tag_name("b")[0].text
        all_emails = ""
        list = []
        for ref_element in wd.find_element_by_id("content").find_elements_by_tag_name("a"):
            if ref_element.text.find('@') >0:
                list.append(ref_element.text)

        all_emails = "\n".join(list)

        return Contact(home=home, work=work, mobile=mobile, phone2=phone2,full_name=full_name,all_emails=all_emails)

    def get_fullinfo_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        return text

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.header_menu_navigation("home")
        wd.find_element_by_xpath(f"//select[@name='to_group']//option[@value='{group_id}']").click()
        wd.find_element_by_xpath("//select[@name='group']//option[@value='[none]']").click()
        wd.find_element_by_xpath(f"//input[@name='selected[]' and @value='{contact_id}']").click()
        wd.find_element_by_name("add").click()
        self.header_menu_navigation("home")

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.header_menu_navigation("home")
        wd.find_element_by_xpath(f"//select[@name='group']//option[@value='{group_id}']").click()
        wd.find_element_by_xpath(f"//input[@name='selected[]' and @value='{contact_id}']").click()
        wd.find_element_by_name("remove").click()
        self.header_menu_navigation("home")