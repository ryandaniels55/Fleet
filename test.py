from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import requests
import pickle


# path = r'/home/ryan/Code/Fleet/geckodriver-v0.31.0-linux64/geckodriver'

# driver = webdriver.Firefox(executable_path = path)

# driver.get('http://example.webscraping.com/search')

# driver.find_element('search_term').send_keys('.')

# js = "document.getElementById('page_size').options[1].text = '100';"
# driver.execute_script(js)

# driver.find_element('search').click()

# driver.implicitly_wait(45)

# links = driver.find_elements_by_css_selector('#results a')

# countries = [link.text for link in links]
# print(countries)
# driver.close()

username = 'ryan.daniels@wattsinnovations.com'

# Instantiate options
opts = Options()
#opts.add_argument(" — headless") # Uncomment if the headless version needed
opts.binary_location = "/usr/lib/firefox/firefox.sh"

# Set the location of the webdriver
firefox_driver = os.getcwd() + '/geckodriver-v0.31.0-linux64/geckodriver'

# Instantiate a webdriver
driver = webdriver.Firefox(options=opts, executable_path=firefox_driver)
# driver.add_cookie(cookies)

# Load the HTML page

cookies = {
    '_ga': 'GA1.2.1782632834.1660594045',
    '_hjSessionUser_2266845': 'eyJpZCI6IjhlM2Q4ODcxLTY3MTQtNWQyYS05ZTBkLWY0OGZiMTVkNmY1MCIsImNyZWF0ZWQiOjE2NjA1OTQwNDUyNTQsImV4aXN0aW5nIjpmYWxzZX0=',
    'AWSALB': 'R66hYWY7sGzCmvbLbsYuWPdYO+BcPISEw5yZ4Hd3gGYlhbyolsSHu+ZxBz3Au+0amkqkYmxRpZtLMn0tSAZ4RVyIfRMYEQLihreqir0u1JEJsRqgQzChD2QaFNId',
    'AWSALBCORS': 'R66hYWY7sGzCmvbLbsYuWPdYO+BcPISEw5yZ4Hd3gGYlhbyolsSHu+ZxBz3Au+0amkqkYmxRpZtLMn0tSAZ4RVyIfRMYEQLihreqir0u1JEJsRqgQzChD2QaFNId',
    '_dd_s': 'rum=1&id=996b01d0-5a4b-41b7-ab90-01659090d42b&created=1660934521269&expire=1660935481270',
}


driver.get('https://suite.auterion.com/authenticated#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUQTRRMEpETkRBM01URTVOVEV6UVRNd1JESkVOVGRFT0VKR04wUkRPRFE1TVVJek5EZzVSZyJ9.eyJodHRwczovL3N1aXRlLmF1dGVyaW9uLmNvbS91c2VyX2lkIjoiMzY5MjkiLCJodHRwczovL3N1aXRlLmF1dGVyaW9uLmNvbS9jb21wYW55Ijoid2F0dHNfaW5ub3ZhdGlvbiIsImlzcyI6Imh0dHBzOi8vbG9naW4uc3VpdGUuYXV0ZXJpb24uY29tLyIsInN1YiI6ImF1dGgwfDYyOWE0MzEwNTgyOTk5MDA2Zjk2ODhhNSIsImF1ZCI6WyJodHRwczovL3N1aXRlLmF1dGVyaW9uLmNvbS9hcGkiLCJodHRwczovL2F1dGVyaW9uLXN1aXRlLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjA5NDcxMzAsImV4cCI6MTY2MDk1NDMzMCwiYXpwIjoiOGpfcHpOdlliY1pmVGRXc0FXUlk5SzRTdDlzSExVelIiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.kcSLBDvFDHePeLhDdcEuFAPrl7dVk24Qewk0BLkfOzQOMcL3N2876HvaX5y-5gm2jhDXO9vsEjunPadJ6TUZt4qcsQ84kIzkO8r_ESD4jyKPgWJb9GV4AYOr0lDlT2yeMmH81eQBMi5qpnnutW6V1L7yc1guz7_BmfbtekY_ZJbnbSSXIIpxexuCoMg1fbsN6K2r2SXMHeT0vwgYPrm0A5vf-wwElfWP20L70105EIg--QKWFCbgFUovTESBY1S0adsytppSJHvVwOEGDqWrfqX17t32_p4CeqqfyCEa4KhOqFOIoJ_Y_CA5KvDmRpkd-AnfeEIkf4A6M_sSnf8Q_w&scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=1EUA20ZwJNzeVOMZCLLiyU~hIckNIF18')

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

driver.implicitly_wait(5)

links = driver.find_elements(By.CSS_SELECTOR, '.email')

soup = BeautifulSoup(driver.page_source, 'html.parser')
email = soup.find('small',class_='.email')
print(soup)

# args = ('css selector', ".email")
# driver.find_element(*args)


# response.find_element(By.class('email rounded-t-md !rounded-b-none'))


# Parse processed webpage with BeautifulSoup
# soup = BeautifulSoup(driver.page_source)
# print(soup.find(id="test").get_text())