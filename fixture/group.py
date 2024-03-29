__author__ = 'Iv.Osipov'

import time


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
        self.fill_group_form(group)
        # submit creation group
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()  # выбрать первую группу
        driver.find_element_by_name("delete").click()  # подтвердить удаление
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()