import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

def test_textbox_interaction():
    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")

    frame_element = driver.find_element(By.ID, 'frame-one1434677811')
    driver.switch_to.frame(frame_element)

    textbox = driver.find_element(By.NAME, 'RESULT_TextField-1')
    textbox.send_keys("Hola")
    time.sleep(2)
    textbox.clear()
    time.sleep(2)
    textbox.send_keys("Hola otra vez")
    time.sleep(2)
    actual_value = textbox.get_attribute('value')

    print(actual_value)