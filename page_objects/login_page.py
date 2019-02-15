"""
This page models the Login page
"""
from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators 
from utils.Wrapit import Wrapit

class Login_Page(Base_Page):
    "This class models the login page"
    username_field = locators.USERNAME_FIELD
    password_field = locators.PASSWORD_FIELD
    submit_button = locators.SUBMIT_BUTTON
    logout_link = locators.LOGOUT_LINK

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)

    @Wrapit._screenshot
    def enter_username(self,username):
        "Set the username"
        result_flag = self.set_text(self.username_field,username)
        self.conditional_write(result_flag,
        positive='Entered the username',
        negative='Could not enter the username',
        level='debug')

        return result_flag

    @Wrapit._screenshot
    def enter_password(self,password):
        "Set the password"
        result_flag = self.set_text(self.password_field, password)

        return result_flag

    @Wrapit._screenshot
    def click_submit(self):
        "Click the submit button"
        result_flag = self.click_element(self.submit_button)

        return result_flag

    @Wrapit._screenshot
    def login(self,username, password):
        "Login to the application"
        result_flag = self.enter_username(username)
        result_flag &= self.enter_password(password)
        result_flag &= self.click_submit()

        return result_flag