#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:26:40 2022

@author: ryan
"""

from selenium.webdriver import Firefox
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait(driver, timeout)

driver_path = os.getcwd() + '/geckodriver-v0.31.0-linux64/geckodriver'

driver = Firefox(executable_path=driver_path)

driver.get('https://suite.auterion.com/flights?type=flight&page=1&sortDirection=desc&sortBy=date')
app = driver.find_element(By.ID,'app')
driver.implicitly_wait(3)

email = driver.find_element(By.CLASS_NAME, 'email')
email.send_keys('ryan.daniels@wattsinnovations.com') #Insert email here

password = driver.find_element(By.CLASS_NAME, 'password')
password.send_keys('xxxxxx') #Insert password here

# args = ('css selector', ".email")
# driver.find_element(*args)


driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div/div/div/button').click() #Login Button

driver.implicitly_wait(10)

recentFlightLogID = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div')

driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/a').click() #Most recent flight log

driver.implicitly_wait(6)

driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/a[3]').click() #Logs Tab

driver.implicitly_wait(3)

driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/button').click() #3 dot button

driver.implicitly_wait(1)

driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/form/button').click() #Original file download button