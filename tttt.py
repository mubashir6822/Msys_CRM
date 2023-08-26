import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()



def automate():
    driver.get('http://127.0.0.1:8000')
    driver.maximize_window()
    driver.find_element(By.XPATH,'/html/body/div/header/div/nav/a').click()
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys('aqheel')
    driver.find_element(By.XPATH,'//*[@id="id_password1"]').send_keys('aqheel1234')#moin1234
    driver.find_element(By.XPATH, '//*[@id="id_password2"]').send_keys('aqheel1234')
    driver.find_element(By.XPATH, '/html/body/div/form/button').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/header/div/a[2]').click()
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys('aqheel')
    driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys('aqheel1234')
    driver.find_element(By.XPATH,'/html/body/div/form/button').click()
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/section/div/div[1]/div[2]/a').click()
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="id_first_name"]').send_keys(input('first_name: '))
    driver.find_element(By.XPATH,'//*[@id="id_last_name"]').send_keys(input('Last_name: '))
    driver.find_element(By.XPATH,'//*[@id="id_age"]').clear()
    driver.find_element(By.XPATH,'//*[@id="id_age"]').send_keys(input('age: '))
    driver.find_element(By.XPATH,'//*[@id="id_agent"]/option[3]').click()
    driver.find_element(By.XPATH,'/html/body/div/form/button').click()
    sleep(2)
    driver.close()
    print('exicuted')
automate()