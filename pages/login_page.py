import locators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        assert self.browser.find_element(*locators.LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*locators.LoginPageLocators.REGISTRATION_FORM), "No registration form"
