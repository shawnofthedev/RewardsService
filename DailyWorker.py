from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Login import TestLogin
from RandomSearch import RandomSeach
import time

 class TestRewards():
 
    # Setup webdriver and navigate to bing
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.bing.com/")
    driver.title # => "Bing"

    # Wait 10 seconds
    # May be able to be removed since edge has become more responsive
    time.sleep(10)

    if driver.find_element(By.ID, "id_n").is_displayed:
        for x in range(50):

            # TODO: Add the ability to check for logged in user 
            # and if not logged in execute login. Login.py test_login.

            # start of login evaluation.
            # if driver.find_element(By.ID, "id_a"):
            #     isHidden = driver.find_element(By.ID).aria_role()
            #     if (isHidden is True):
            #         driver.find_element(By.ID, "id_a").click()
            # else:

            driver.find_element(By.ID, "sb_form_q").click()
            driver.find_element(By.ID, "sb_form_q").clear()
            input_text = RandomSeach.generate_string()
            driver.find_element(By.ID, "sb_form_q").send_keys(input_text)
            driver.find_element(By.ID, "sb_form_q").send_keys(Keys.ENTER)
            driver.implicitly_wait(1)

            

    driver.implicitly_wait(10)
    driver.quit()
