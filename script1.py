import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
driver.maximize_window()

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

username.send_keys("phiteshvarma@gmail.com")
password.send_keys("Qwerty123asd")

btn = driver.find_element_by_id("loginbutton")
btn.click()

profile = driver.find_elements_by_css_selector('#u_0_c > a:nth-child(1)')
#profile = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/a')
profile.click()
