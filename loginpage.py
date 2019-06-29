from time import sleep
from selenium.webdriver.common.by import By
from base.genric_findelement import FindElement
import time
from base import genric_screenshot

class LoginPage(FindElement):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

     #stroing the Attribute value in the variable
    _username='username'
    _password='pwd'
    _login='loginButton'

# *********************************************************************

    def enterUsername(self,usn):
        self.sendKeys(usn,'id',self._username)

    def enterPassword(self,pwd):
        self.sendKeys(pwd,'name',self._password)

    def clickLoginButton(self):
        self.clickOnElement('id',self._login)

# *********************************************************************

    def login(self,usn,pwd):
        self.enterUsername(usn)
        sleep(2)
        self.enterPassword(pwd)
        sleep(2)
        self.clickLoginButton()


    def verifyTitle(self):
        sleep(2)
        expected_title = 'actiTIME - Enter Time-Track'
        actual_title = self.driver.title

        if expected_title != actual_title:
            genric_screenshot.takeScreenshot(self.driver)
            assert expected_title==actual_title




