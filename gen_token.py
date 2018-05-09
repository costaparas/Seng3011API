#!/usr/bin/env python3
#Generate a Facebook Graph API token dynamically
#Based largely on https://gist.github.com/ManrajGrover/ba1bd439d3d5a59feaaf

import os
from selenium import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#navigate to fb login page
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get('https://www.facebook.com/')

#provide credentials of placeholder fb account
email = driver.find_element_by_id('email')
email.send_keys('event.stock1@gmail.com')
passwd = driver.find_element_by_id('pass')
passwd.send_keys(os.environ['FB_PASSWD'])

#login to fb
login = driver.find_element_by_id('loginbutton')
login.click()

#navigate to the graph explorer page
driver.get('https://developers.facebook.com/tools/explorer/')

#find and click "Get Token"
button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[2]/a')
button.click()

#find and click "Get User Access Token"
button = driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]/a')
button.click()

#find and click "Get Access Token"
button = driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div/button[1]')
button.click()

#get value of token
token = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div/div[1]/label/input')
print(token.get_attribute('value'))

driver.quit()