class GroupHelper:

    def __init__(self, app):
        self.app = app

    def type_group_property(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def create(self, group):
        wd = self.app.wd
        self.header_menu_navigation("groups")
        # add new group
        wd.find_element_by_name("new").click()
        self.fill_group_info(group)
        wd.find_element_by_name("submit").click()
        self.return_to_elements_page("group page")

    def fill_group_info(self, group):
        self.type_group_property("group_name", group.name)
        self.type_group_property("group_header", group.header)
        self.type_group_property("group_footer", group.footer)

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
        wd.find_element_by_xpath(f"//input[@type='checkbox' and @title='Select ({search_filter})']").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_info(group)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_elements_page("group page")
        self.header_menu_navigation("home")

    def return_to_elements_page(self, items):
        wd = self.app.wd
        wd.find_element_by_link_text(items).click()

    def header_menu_navigation(self, item):
        wd = self.app.wd
        if item == 'groups':
            if (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
                return
        if item == 'home':
            if (len(wd.find_elements_by_id("search_count")) > 0):
                return
        wd.find_element_by_link_text(item).click()

    def count(self):
        wd = self.app.wd
        self.header_menu_navigation("groups")
        return len(wd.find_elements_by_name("selected[]"))

    def exists(self, search_filter):
        wd = self.app.wd
        self.header_menu_navigation("groups")
        # count
        if len(wd.find_elements_by_xpath(f"//input[@type='checkbox' and @title='Select ({search_filter})']")) > 0:
            return True
        return False