import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/ghtayeg/PycharmProjects/pythonProject/driver/chromedriver.exe")
#driver.set_page_load_timeout(10)
driver.get("https://www.talan-academy.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='main-menu']/div/div/div/nav/div/ul/li[5]/a").click()
time.sleep(4)
assert driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/div[3]/p[2]/span").is_displayed()


time.sleep(4)
driver.quit()