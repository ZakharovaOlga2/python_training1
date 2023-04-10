# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroupPy(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def test_add_group_py(self):
        wd = self.wd
        self.go_to_home_page(wd, "http://localhost/addressbook/")
        self.login(wd, login="admin", password="secret")
        self.add_new_group(wd, Group("21212", "vsdvsdvsd", "ebrbsf d"))
        self.logout(wd)

    def test_add_empty_group_py(self):
        wd = self.wd
        self.go_to_home_page(wd, "http://localhost/addressbook/")
        self.login(wd, login="admin", password="secret")
        self.add_new_group(wd, Group("", "", ""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def add_new_group(self, wd, group):
        self.header_menu_navigation(wd, "groups")
        # add new group
        wd.find_element_by_name("new").click()
        # group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # group header
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        # group footer
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_elements_page(wd, "group page")

    def return_to_elements_page(self, wd, items):
        wd.find_element_by_link_text(items).click()

    def header_menu_navigation(self, wd, item):
        wd.find_element_by_link_text(item).click()

    def login(self, wd, login, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def go_to_home_page(self, wd, url):
        wd.get(url)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
