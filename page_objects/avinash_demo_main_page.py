"""
Page object for iOS Demo main Page.
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
from Mobile_Base_Page import Mobile_Base_Page


class Avinash_Demo_Main_Page(Mobile_Base_Page):
    "Page object bitcoin main page."

    #Locators of the mobile page elements.
    demo_name_input = locators.demo_name_input
    demo_phone_input = locators.demo_phone_input
    demo_submit_button = locators.demo_submit_button


    @Wrapit._screenshot
    def set_name_input(self,name):
        "This method is to set name in demo app main page"
        result_flag = self.set_text(self.demo_name_input,name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'%name,
            negative='Failed to set the name to: %s'%name,
            level='debug')

        return result_flag

    @Wrapit._screenshot
    def set_phone_input(self,phone):
        "This method is set phone no in demo app main page"
        result_flag = self.set_text(self.demo_phone_input,phone)
        self.conditional_write(result_flag,
            positive='Set the phone no to: %s'%phone,
            negative='Failed to set the phone no to: %s'%phone,
            level='debug')

        return result_flag

    @Wrapit._screenshot
    def set_name_input(self,name):
        "This method is to set name in demo app main page"
        result_flag = self.set_text(self.demo_name_input,name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'%name,
            negative='Failed to set the name to: %s'%name,
            level='debug')

        return result_flag

    @Wrapit._screenshot
    def click_submit(self):
        "This method is used to click submit button in demo app main page"
        result_flag = self.click_element(self.demo_submit_button)
        self.conditional_write(result_flag,
            positive='Able to click on submit button',
            negative='Unable to click on submit button',
            level='debug')

        return result_flag



            

    

            

        
        
       




