"""
This class models the login page of the Qxf2 trainer app
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Login_Page(Base_Page):
    "Page object for the login page"
    USERNAME = locators.USERNAME
    PASSWORD = locators.PASSWORD
    SUBMIT_BUTTON = locators.LOGIN_SUBMIT
    LOGOUT_LINK = locators.LOGOUT_LINK

    def start(self):
        "Open this page"
        self.open('')

    def set_username(self,username):
        "Set the username"
        result_flag = self.set_text(self.USERNAME,username)
        self.conditional_write(result_flag,
        positive='Set the username',
        negative='Could not set the username',
        level='debug')

        return result_flag

    def set_password(self,password):
        "Set the password"
        result_flag = self.set_text(self.PASSWORD,password)
        self.conditional_write(result_flag,
        positive='Set the password',
        negative='Could not set the password',
        level='debug')

        return result_flag

    def click_submit(self):
        "Click the submit button"
        result_flag = self.click_element(self.SUBMIT_BUTTON)
        self.conditional_write(result_flag,
        positive='Clicked the login submit button',
        negative='Could not click the login submit button',
        level='debug')

        return result_flag

    def login(self,username,password):
        "Login to the application"
        result_flag = self.set_username(username)
        result_flag &= self.set_password(password)
        result_flag &= self.click_submit()
        result_flag &= self.check_element_present(self.LOGOUT_LINK)
        
        return result_flag
        