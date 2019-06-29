from selenium.webdriver.common.by import By
import logging

class FindElement():

    def __init__(self,driver):
        self.driver=driver

    logging.basicConfig(filename='test1.log',level=logging.INFO)

    def getByType(self,locator_name):

        locator_name=locator_name.lower()

        if locator_name=='id':
            return By.ID
        elif locator_name=='name':
            return By.NAME
        elif locator_name=='class_name':
            return By.CLASS_NAME
        elif locator_name=='xpath':
            return By.XPATH
        else:
            logging.info(('locator ==> ',locator_name,' not found'))
        return False

    def getElement(self,locator_value,locator_name):
        element=None
        try:
            locator_name=locator_name.lower()
            bytype=self.getByType(locator_name)
            element=self.driver.find_element(bytype,locator_value)
            logging.info(('element found with locator name ==> ',locator_name
                  ,'with locator value ==> ',locator_value))
        except:
            logging.info('element not found with locator name ==> ',locator_name
                  ,'with locator value ==> ',locator_value)
        return element

    def clickOnElement(self,locator_name,locator_value):
        try:
            element=self.getElement(locator_value,locator_name)
            element.click()
            logging.info(('clicked on a element with locator name ==> ',locator_name
                  ,'with locator value ==> ',locator_value))
        except:
            logging.info('cannot click on a element with locator name ==> ',locator_name
                  ,'with locator value ==> ',locator_value)

    def sendKeys(self,message,locator_name,locator_value):
        try:
            element=self.getElement(locator_value, locator_name)
            element.send_keys(message)
            logging.info(('sent data on a element with locator name ==> ', locator_name,'with locator value ==> ', locator_value))
        except:
            logging.info('cant send data on a element with locator name ==> ', locator_name,'with locator value ==> ', locator_value)









