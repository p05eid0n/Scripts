#Basic facebook login script

import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
driver.maximize_window()

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

username.send_keys("")  #enter the username
password.send_keys("")  #enter the password

btn = driver.find_element_by_id("loginbutton")
btn.click()

