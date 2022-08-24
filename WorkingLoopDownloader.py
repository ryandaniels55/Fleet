#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:02:59 2022

@author: ryan
"""

from selenium.webdriver import Firefox
import os
from pathlib import Path
from pyulog import ulog2csv
import time
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import RC_Control_Loss_Script as RC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait(driver, timeout)

cur = os.getcwd()

driver_path = cur + '/geckodriver-v0.31.0-linux64/geckodriver'

driver = Firefox(executable_path=driver_path)

previousFlightLogID = '1' # initialize previousFlightLogID as any variable

while True:
    
    time.sleep(5)
    driver = Firefox(executable_path=driver_path)
    driver.get('https://suite.auterion.com/flights?type=flight&page=1&sortDirection=desc&sortBy=date')
    app = driver.find_element(By.ID,'app')
    driver.implicitly_wait(10)

    email = driver.find_element(By.CLASS_NAME, 'email')
    email.send_keys('ryan.daniels@wattsinnovations.com') # Insert email here

    password = driver.find_element(By.CLASS_NAME, 'password')
    password.send_keys('xxxxx') # Insert password here

    driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div/div/div/button').click() # Login Button

    driver.implicitly_wait(15)

    recentFlightLogID = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div').get_attribute('innerHTML')
    recentFlightLogID = recentFlightLogID[:6]

    if recentFlightLogID == previousFlightLogID:
        
        previousFlightLogID = recentFlightLogID
        print('No new flight logs')
        time.sleep(5)
        driver.quit()
    
    
    if recentFlightLogID != previousFlightLogID:
            
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/a').click() #Most recent flight log
        driver.implicitly_wait(10)
        
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/a[3]').click() #Logs Tab
        driver.implicitly_wait(10)
        
        time.sleep(2)
        ulog_name = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/a').get_attribute('innerHTML')
        ulog_name = ulog_name[:29]
        
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/button').click() #3 dot button
        driver.implicitly_wait(10)
            
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/form/button').click() #Original file download button
        
        print('New flight log detected, downloading now')
        time.sleep(5)
        driver.quit()
        
        # moving ulog from download folder into it's own folder
        
        downloads_path = str(Path.home() / "Downloads")+'/'
        recentFlightLogID_ulog = recentFlightLogID+'.ulg'
        os.rename(downloads_path+ulog_name, downloads_path+recentFlightLogID_ulog)
        output = cur+'/csv'+'/'+recentFlightLogID
        csv_output = cur+'/csv'+'/'+recentFlightLogID
        ulog_output = cur+'/ulog'+'/'+recentFlightLogID
        os.makedirs(csv_output, exist_ok=True)
        os.makedirs(ulog_output, exist_ok=True)
        shutil.move(os.path.join(downloads_path,recentFlightLogID_ulog), os.path.join(ulog_output,recentFlightLogID_ulog))
        
        previousFlightLogID = recentFlightLogID
        
        # ulog to csv new flight log
        
        os.chdir(ulog_output)
        ulog2csv.convert_ulog2csv(recentFlightLogID_ulog, [], csv_output, ',')
        
        # change to csv directory
        
        os.chdir(csv_output)
        
        # DATA ANALYSIS GOES HERE
        
        if __name__ == '__main__':
            
            RC.RC_control_loss(recentFlightLogID)
        
        # winch0 = recentFlightLogID+'_winch_status_0.csv'
        # winchdata = output+'/'+winch0

        # wdata = pd.read_csv(winchdata)
        
        
        
        
        