from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = "Iv.Osipov"


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)

    def destroy(self):
        self.driver.quit()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()


    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()


    def create_group(self, group):
        driver = self.driver
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


    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()


    def login(self, login, password):
        driver = self.driver
        self.open_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()


    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


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