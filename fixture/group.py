__author__ = 'Iv.Osipov'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()



    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # init group page creation
        driver.find_element_by_name("new").click()
        # fill group fields
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit creation group
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()  # выбрать первую группу
        driver.find_element_by_name("delete").click()  # подтвердить удаление
        self.return_to_groups_page()



    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()