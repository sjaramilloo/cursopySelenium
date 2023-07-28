import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def test_textbox_interaction():
    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")

    source = driver.find_element(By.XPATH, "//*[@class='class=ui-widget-content ui-draggable ui-draggable-handle' and text() = 'Drag me to my target']")
    target = driver.find_element(By.ID, 'droppable')

    action = ActionChains(driver)

    action.drag_and_drop(source, target).perform()
    time.sleep(5)