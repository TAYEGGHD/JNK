import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/ghtayeg/PycharmProjects/pythonProject/driver/chromedriver.exe")
#driver.set_page_load_timeout(10)
driver.get("https://www.talan-academy.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='main-menu']/div/div/div/nav/div/ul/li[5]/a").click()
time.sleep(3)
assert driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/div[3]/p[2]/span").is_displayed()
time.sleep(3)
driver.find_element(By.ID, "inputEmail").send_keys("ghada.tayeg@talan.com")
time.sleep(2)
driver.find_element(By.ID, "inputPassword").send_keys("DmbDBgDbHT95")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[3]/form/div[3]/button").click()
time.sleep(2)
driver.find_element(By.ID, "fa-angle-main-nav").click()
time.sleep(1)
driver.find_element(By.ID, "userAccount").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/h4/span/span/a[1]").click()
time.sleep(1)
driver.find_element(By.ID, "student_city").send_keys("Tunis")
time.sleep(1)
driver.find_element(By.ID, "student_save").click()

time.sleep(4)
driver.quit()
