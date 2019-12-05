from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
__author__ = "Iv.Osipov"

# Класс представляет собой фикстуру
class Application:

    def __init__(self):
        self.driver = WebDriver()# инциаилизурем веб драйвер

        self.driver.implicitly_wait(60)  # выставляем неявные ожидания в 1 мин
        self.session = SessionHelper(self)  # инициализируем помощника по работе с сессиями
        self.group = GroupHelper(self)  # инициализируем помощника по работе с группами

    def destroy(self):
        self.driver.quit()



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