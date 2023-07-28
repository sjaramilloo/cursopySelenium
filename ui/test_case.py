from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.pl/index.php')
    driver.maximize_window()
    web_element = driver.find_elements(By.CLASS_NAME, 'sf-with-ul')
    print("Cantidad de elementos Clase: ", len(web_element))
    web_element[3].click()
    time.sleep(3)
    web_element = driver.find_element(By.CLASS_NAME, 'class="button ajax_add_to_cart_button btn btn-default"')
    web_element[3].click()
    time.sleep(3)


    #driver.find_element(By.CLASS_NAME, 'sf-with-ul').click()