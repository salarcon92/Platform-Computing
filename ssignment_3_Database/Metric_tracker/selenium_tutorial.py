from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# navigate browser
driver.back()
driver.forward()
driver.refresh()

driver.get("https://selenium.dev")
  
title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()