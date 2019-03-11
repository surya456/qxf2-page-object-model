"""
This module models the login page of our Qxf2 Trainer application
"""
from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Login_Page(Base_Page):
    "The login page class"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)

    @Wrapit._screenshot
    def enter_username(self,username):
        "Enter the username"
        result_flag = self.set_text(locators.USERNAME_FIELD,username)
        self.conditional_write(result_flag,
        positive='Entered the username %s'%username,
        negative='Could not enter the username field!',
        level='debug')

        return result_flag
    
    @Wrapit._screenshot
    def enter_password(self,password):
        "Enter the password"
        result_flag = self.set_text(locators.PASSWORD_FIELD,password)
        self.conditional_write(result_flag,
        positive='Entered the password',
        negative='Could not enter the password',
        level='debug')

        return result_flag

    @Wrapit._screenshot
    def click_login_button(self):
        "Click the login button"
        result_flag = self.click_element(locators.LOGIN_BUTTON)
        self.conditional_write(result_flag,
        positive='Clicked the login button',
        negative='Could not click the login button',
        level='debug')

        return result_flag

    def verify_login_happened(self):
        "Verify the presence of the logout link"
        result_flag = self.check_element_present(locators.LOGOUT_LINK)
        self.conditional_write(result_flag,
        positive='Login worked. Logout link is present.',
        negative='Could not login. Automation did not notice the logout link.',
        level='debug')

        if result_flag:
            self.switch_page('Home')

        return result_flag

    def login(self,username,password):
        "Login to the application"
        result_flag = self.enter_username(username)
        result_flag &= self.enter_password(password)
        result_flag &= self.click_login_button()
        result_flag &= self.verify_login_happened()

        return result_flag
