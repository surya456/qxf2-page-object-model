"""
This module models the menu object of the Qxf2 tutorial application
"""

import conf.locators_conf as locators 

class Menu_Object():
    "This class models the menu object"
    logout_link = locators.LOGOUT_LINK
    
    def logout(self):
        "Logout of the applications"
        result_flag = self.click_element(self.logout_link)
        result_flag &= not self.check_element_present(self.logout_link)

        return result_flag