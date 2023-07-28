import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

def test_textbox_interaction():
    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")

    calendario = driver.find_element(By.ID, 'datepicker')

    calendario.click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text() = '23']").click()
    time.sleep(2)
    calendario.click()
    driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text() = '14']").click()
    time.sleep(4)

    calendario.clear()
    calendario.send_keys('01/01/2001')

    time.sleep(5)