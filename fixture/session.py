__author__ = 'Iv.Osipov'

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, login, password):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()