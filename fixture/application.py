from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def add_new_group(self, group):
        wd = self.wd
        self.header_menu_navigation("groups")
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
        self.return_to_elements_page("group page")

    def return_to_elements_page(self, items):
        wd = self.wd
        wd.find_element_by_link_text(items).click()

    def header_menu_navigation(self, item):
        wd = self.wd
        wd.find_element_by_link_text(item).click()

    def go_to_home_page(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()