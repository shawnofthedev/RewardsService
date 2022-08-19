from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():

    # def setup_method(self, method):
    #     self.driver = webdriver.Chrome()
    #     self.vars = {}
  
    # def teardown_method(self, method):
    #     self.driver.quit()

  
    def test_login(self):
        self.driver.find_element(By.ID, "id_a").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .id_link_text").click()
        self.driver.find_element(By.ID, "i0116").send_keys("svotaw81@hotmail.com")
        self.driver.find_element(By.ID, "i0118").send_keys("Owen91416")
        self.driver.find_element(By.ID, "idSIButton9").click()
        element = self.driver.find_element(By.ID, "idSIButton9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "idSIButton9").click()
  
