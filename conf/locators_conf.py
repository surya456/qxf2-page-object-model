#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the login page 
USERNAME = "name,username"
PASSWORD = "xpath,//input[@name='password']"
LOGIN_SUBMIT = "xpath,//button[contains(@class,'btn-danger')]"

#Menu objects
LOGOUT_LINK = "xpath,//a[text()='Logout']"