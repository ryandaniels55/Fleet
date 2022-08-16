# Importing libraries
import time
import hashlib
from pprint import pprint
import datetime
import pandas as pd
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

cookies = {
    '_ga': 'GA1.2.1782632834.1660594045',
    '_gid': 'GA1.2.1348339576.1660594045',
    '_hjSessionUser_2266845': 'eyJpZCI6IjhlM2Q4ODcxLTY3MTQtNWQyYS05ZTBkLWY0OGZiMTVkNmY1MCIsImNyZWF0ZWQiOjE2NjA1OTQwNDUyNTQsImV4aXN0aW5nIjpmYWxzZX0=',
    'AWSALB': 'bgp968N3tgdC0Yqom4phrbH1MdXyNrDxsY5/HMDqp+YFn+7lSuqNKjB5dPTQAdZv/XLj5xNi01QDkERiFJ8V6yknSmCSrRXQmY5Yhh0z2bzMHbqOJgESvvTGa+44',
    'AWSALBCORS': 'bgp968N3tgdC0Yqom4phrbH1MdXyNrDxsY5/HMDqp+YFn+7lSuqNKjB5dPTQAdZv/XLj5xNi01QDkERiFJ8V6yknSmCSrRXQmY5Yhh0z2bzMHbqOJgESvvTGa+44',
    '_dd_s': 'rum=1&id=b9894720-352e-41cb-aa50-5753cbbfe8e4&created=1660676681669&expire=1660677602043',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.1782632834.1660594045; _gid=GA1.2.1348339576.1660594045; _hjSessionUser_2266845=eyJpZCI6IjhlM2Q4ODcxLTY3MTQtNWQyYS05ZTBkLWY0OGZiMTVkNmY1MCIsImNyZWF0ZWQiOjE2NjA1OTQwNDUyNTQsImV4aXN0aW5nIjpmYWxzZX0=; AWSALB=bgp968N3tgdC0Yqom4phrbH1MdXyNrDxsY5/HMDqp+YFn+7lSuqNKjB5dPTQAdZv/XLj5xNi01QDkERiFJ8V6yknSmCSrRXQmY5Yhh0z2bzMHbqOJgESvvTGa+44; AWSALBCORS=bgp968N3tgdC0Yqom4phrbH1MdXyNrDxsY5/HMDqp+YFn+7lSuqNKjB5dPTQAdZv/XLj5xNi01QDkERiFJ8V6yknSmCSrRXQmY5Yhh0z2bzMHbqOJgESvvTGa+44; _dd_s=rum=1&id=b9894720-352e-41cb-aa50-5753cbbfe8e4&created=1660676681669&expire=1660677602043',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'type': 'flight',
    'page': '1',
    'sortDirection': 'desc',
    'sortBy': 'date',
}

response = requests.get('https://suite.auterion.com/flights?page=1&sortDirection=desc&sortBy=date', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')


# setting the URL you want to monitor
url = Request('https://suite.auterion.com/flights?page=1&sortDirection=desc&sortBy=date&type=flight',
              headers=headers)
 
# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()
 
# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
         
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
         
        # wait for 30 seconds
        time.sleep(30)
         
        # perform the get request
        response = urlopen(url).read()
         
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
 
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print('still running')
            continue
 
        # if something changed in the hashes
        else:
            # notify
            print("something changed")
 
            # again read the website
            response = urlopen(url).read()
 
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
 
            # wait for 30 seconds
            time.sleep(30)
            continue
             
    # To handle exceptions
    except Exception as e:
        print("error")