"""
This module models the menu bar of the Qxf2 trainer app
"""
import conf.locators_conf as locators

class Navigation_Object:
    "This class is for the navigation object"

    def click_logout(self):
        "Click the logout link"
        result_flag = self.click_element(locators.LOGOUT_LINK)
        self.conditional_write(result_flag,
        positive='Clicked the logout link',
        negative='Could not click the logout link',
        level='debug')

        return result_flag

    def verify_logout_happened(self):
        "Verify logout happened and that the username field is seen"
        result_flag = self.check_element_present(locators.USERNAME_FIELD)
        self.conditional_write(result_flag,
        positive='Logout succeeded. I see the username field.',
        negative='Could not logout. Automation does not notice the username field.',
        level='debug')

        return result_flag

    def logout(self):
        "Logout of the Qxf2 Trainer application"
        result_flag = self.click_logout()
        result_flag &= self.verify_logout_happened()

        return result_flag