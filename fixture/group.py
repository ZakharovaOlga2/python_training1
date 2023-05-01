from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
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
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_elements_page("group page")

    def delete_first_group(self):
        wd = self.app.wd
        self.header_menu_navigation("groups")
        # select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        #return
        self.return_to_elements_page("group page")

    def modify(self, search_filter, group):
        wd = self.app.wd
        self.header_menu_navigation("groups")
        # edit instance or exit (if there are no results)
        try:
            wd.find_element_by_xpath(f"//input[@type='checkbox' and @title='Select ({search_filter})']").click()
        except NoSuchElementException:
            self.header_menu_navigation("home")
            return
        wd.find_element_by_name("edit").click()
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
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_elements_page("group page")
        self.header_menu_navigation("home")


    def return_to_elements_page(self, items):
        wd = self.app.wd
        wd.find_element_by_link_text(items).click()

    def header_menu_navigation(self, item):
        wd = self.app.wd
        wd.find_element_by_link_text(item).click()