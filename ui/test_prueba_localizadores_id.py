from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.ID, "field2").send_keys("Juan")
    time.sleep(5)


