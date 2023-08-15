from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Information import info
from Test_Location import location
import pytest
from Test_Information import add
from Test_Location import location
from Test_Location import pimlocation 
from Test_Location import emplistloc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Test_suite
class Test_project:  
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))        
        yield
        self.driver.close()
   
    # valid login testing
    def test_login1(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=location.Location().username_input_box).send_keys(info.Info().username)
        self.driver.find_element(by=By.NAME, value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        assert self.driver.title == 'OrangeHRM'
        print("the user is logged in successfully")
        print('SUCCESS : Logged in with Username {a} and {b}'.format(a=info.Info().username, b=info.Info().password))

    def test_pim_add_employee(self,startup): 
        #if it logins successfully it goes to pim module in leftside portal  
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click() 

            #to add employee details +add button is clicked
           self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

            #add employee using Add Employee button        
            #self.driver.find_element(by=By.XPATH, value="//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
             
           self.driver.find_element(by=By.NAME,value=pimlocation.Pimlocation().firstname_input_box).send_keys(add.Add().firstName)
           self.driver.find_element(by=By.NAME,value=pimlocation.Pimlocation().middlename_input_box).send_keys(add.Add().middleName)
           self.driver.find_element(by=By.NAME,value=pimlocation.Pimlocation().lastname_input_box).send_keys(add.Add().lastName)
           self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().create_login_details).click()
           self.driver.find_element(by=By.XPATH,value=pimlocation.Pimlocation().Username).send_keys(add.Add().Username)
           self.driver.find_element(by=By.XPATH,value=pimlocation.Pimlocation().password).send_keys(add.Add().password)
           self.driver.find_element(by=By.XPATH,value=pimlocation.Pimlocation().confirm_password).send_keys(add.Add().confirm_password)
           if(self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().status_disabled)):
                            self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().status_disabled).click()
           self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().save_button).click() 
           assert self.driver.find_element(by=By.CSS_SELECTOR, value=pimlocation.Pimlocation().save_css).click()
           
           


    def test_pimdelete(self,startup):  
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           #pim
           self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click() 
           #to click employee list
           employee_list=self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
           action = ActionChains(self.driver)
           action.click(on_element=employee_list).perform()
           self.driver.find_element(by=By.LINK_TEXT, value='Employee List').click()
           self.driver.find_element(by=By.XPATH, value=emplistloc.Emplist.employee_name).send_keys(add.Add().del_user)
           self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().search).click()
           self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().delete_button).click()
           self.driver.find_element(by=By.XPATH, value=pimlocation.Pimlocation().confirm_delete).click()
           assert self.driver.find_element(by=By.CSS_SELECTOR, value=pimlocation.Pimlocation().save_css).click()
           print("successfully deleted employee details [deleted employee:{a}]".format(a=add.Add().del_user))
             