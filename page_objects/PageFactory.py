"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Login page
"""

from page_objects.login_page import Login_Page
from page_objects.home_page import Home_Page

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url='http://qxf2trainer.pythonanywhere.com/',trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "login page" or page_name == "login":
            test_obj = Login_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "home page" or page_name == "home":
            test_obj = Home_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)

        return test_obj

    get_page_object = staticmethod(get_page_object)