"""
This module models the menu object
"""

from utils.Wrapit import Wrapit
import conf.locators_conf as locators  


class Menu_Object():
    "Class to model the Menu object"

    def verify_logout(self):
        "Verify that we are on the login page after a logout"
        result_flag = self.check_element_displayed(locators.USERNAME_FIELD)
        self.conditional_write(result_flag,
        positive='Automation is on the login page',
        negative='Automation could not find the username field. Are we really on the login page?',
        level='debug')

        return result_flag

    def logout(self):
        "Click the logout link"
        result_flag = self.click_element(locators.LOGOUT_LINK)
        self.conditional_write(result_flag,
        positive='I clicked the logout link',
        negative='I could not click the logout link',
        level='debug')
        result_flag &= self.verify_logout()

        return result_flag
