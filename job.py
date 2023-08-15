from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Information import add
from Test_Location import location
from Test_Location import pimlocation 
from Test_Location import emplistloc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import pyautogui
import time


class Orangehrm:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(50)
    #login1 : successful employee login to orangeHRM portal
    def login(self):
        self.driver.find_element(by=By.NAME,value=location.Location().username_input_box).send_keys(info.Info().username)
        self.driver.find_element(by=By.NAME,value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
            print("the user is logged in successfully") 

    def pim_job_employee(self): 
            #pim
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click() 
            
            self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.employee_list_name).send_keys(add.Add().del_user)                                                                                    
            self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().search).click()  
            time.sleep(6)
            print("get into aahamed ahahiq M record")                        
            self.driver.find_element(by=By.XPATH,value=emplistloc.Emplist.select_record).click()
            time.sleep(6)
            
            #JOB DETAILS:
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.view_job).click()
            #ACTION CHAINS
            print("ACTION CHAINS USED")
            #job_title
            job_title = self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.job_title)
            action = ActionChains(self.driver)
            action.click(on_element=job_title).perform()
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.qalead).click()
            print("JOB TITLE selected in dropdown")
            #job category
            job_category = self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.job_category)
            action = ActionChains(self.driver)
            action.click(on_element=job_category).perform()
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.professional).click()
            print("JOB CATEGORY selected in drop down")
            #sub unit
            sub_unit = self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.sub_unit)
            action = ActionChains(self.driver)
            action.click(on_element=sub_unit).perform()
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.quality_assurance).click()
            print("SUB UNIT selected in drop down")
            #location
            location= self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.location)
            action = ActionChains(self.driver)
            action.click(on_element=location).perform()
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.locans).click()
            print("LOCATION selected in dropdown")
            #employment status
            emp_status = self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.emp_status)
            action = ActionChains(self.driver)
            action.click(on_element=emp_status).perform()
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.fulltime).click()
            print("EMPLOYMENT STATUS selected in drop down")
            self.driver.find_element(by=By.XPATH,value = emplistloc.Emplist.savejob).click()
            print("SUCCESSFULLY JOB DETAILS UPDATED")

orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.pim_job_employee()
            