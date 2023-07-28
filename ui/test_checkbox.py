import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

def test_checkbox_interaction():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    frame_element = driver.find_element(By.ID, 'frame-one1434677811')
    driver.switch_to.frame(frame_element)

    checkbox = driver.find_element(By.NAME, 'RESULT_CheckBox-8')
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(3)
    #checkbox.click()
    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(3)

    print("Tipo de elemento:", checkbox.get_attribute('type'))
    print("Seleccionado: ", checkbox.is_selected())