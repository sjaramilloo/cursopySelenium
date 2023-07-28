import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_textbox_interaction():
    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")

    time.sleep(3)
    select_file= Select(driver.find_element(By.NAME, 'files'))

    select_file.select_by_value('3')

    time.sleep(5)

    select_file.select_by_visible_text('Other file')
    time.sleep(5)