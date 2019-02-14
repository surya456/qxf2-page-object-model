"""
This page models the login page of the Qxf2 trainer app
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Login_Page(Base_Page):
    "Class to model the login page"
    
    #Locators
    username_field = locators.USERNAME_FIELD
    password_field = locators.PASSWORD_FIELD
    submit_button = locators.SUBMIT_BUTTON
    logout_link = locators.LOGOUT_LINK

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)

    def login(self,username,password):
        "Login to the app"
        result_flag = self.set_username(username)
        result_flag &= self.set_password(password)
        result_flag &= self.click_submit_button()
        result_flag &= self.verify_login_worked()

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_username(self,username):
        "Set the username"
        result_flag = self.set_text(self.username_field,username)
        self.conditional_write(result_flag,
        positive='Set the username',
        negative='Could not set the username',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self,password):
        "Set the password"
        result_flag = self.set_text(self.password_field,password)
        self.conditional_write(result_flag,
        positive='Set the password',
        negative='Could not set the password',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_submit_button(self):
        "Click the submit button"
        result_flag = self.click_element(self.submit_button)
        self.conditional_write(result_flag,
        positive='Clicked the submit button',
        negative='Could not click the submit button',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def verify_login_worked(self):
        "Verify the login worked"
        result_flag = self.check_element_present(self.logout_link)
        self.conditional_write(result_flag,
        positive='Located the logout link after login',
        negative='Could not locate the logout link after login',
        level='debug')

        return result_flag