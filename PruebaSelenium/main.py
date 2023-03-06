from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://computer-database.gatling.io/computers")



web_elemet = driver.find_element(By.ID, 'add').click()
web_elemet = driver.find_element(By.NAME, 'name')
web_elemet.send_keys("Nombre de computador")
web_elemet = driver.find_element(By.NAME, 'introduced')
web_elemet.send_keys("1991-02-23")
web_elemet = driver.find_element(By.NAME, 'discontinued')
web_elemet.send_keys("1994-07-16")
web_elemet = driver.find_element(By.ID, 'company')
select_object = Select(web_elemet)
select_object.select_by_value('1')

web_elemet = driver.find_element(By.CLASS_NAME, 'btn').click()






time.sleep(15)



