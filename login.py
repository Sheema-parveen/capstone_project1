#PROJECT1
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Information import invalid_info
from Test_Location import location
from selenium.webdriver.common.by import By

class Orangehrm:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(25)
    #login1 : successful employee login to orangeHRM portal
    def login(self):
        self.driver.find_element(by=By.NAME,value=location.Location().username_input_box).send_keys(info.Info().username)
        self.driver.find_element(by=By.NAME,value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
            print("the user is logged in successfully")

    #login2: invalid employee login to orangeHRM portal
    def invalid_login(self):
        self.driver.find_element(by=By.NAME,value=location.Location().username_input_box).send_keys(invalid_info.Invalid_info().username)
        self.driver.find_element(by=By.NAME,value=location.Location().password_input_box).send_keys(invalid_info.Invalid_info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        if(self.driver.current_url != "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
            print("A valid error message for invalid credentials is displayed")
    #shutdown
    def shutdown(self):
        self.driver.quit()

#object1 : orangehrm  used for successful login 
orangehrm = Orangehrm(info.Info().url)
orangehrm.login()


#object2: orangehrm1 used for invalid login
orangehrm1 = Orangehrm(invalid_info.Invalid_info().url)
orangehrm1.invalid_login()
orangehrm1.shutdown()

