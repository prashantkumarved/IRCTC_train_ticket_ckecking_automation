from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from datetime import date
import os

# python code and logic for dynamic input

station_from = input('enter starting station: ').upper()
# for starting station validation
n = True
while n:
    fhand = open('stations.txt')
    for line in fhand:
        if station_from in line:
            # print(line)
            station_from = line.rstrip ()
            print(station_from)
            n = False
            break
    else:
        station_from = input('station not found, please enter valid station:').upper()

# # for ending station validation
station_to = input('enter destination station: ').upper()
m = True
while m:
    fhand = open('stations.txt')
    for line in fhand:
        if station_to in line:
            # print(line)
            station_to = line.rstrip()
            print(station_to)
            m = False
            break
    else:
        station_to = input('station not found, please enter valid station:').upper()


# for date
#
day = int(input('enter day in numeric form: '))
if day< 10:
    Day = '0'+str(day)
else:
    Day = str(day)
month = int(input('enter month in numeric form: '))
if month< 10:
    Month = '0'+str(month)
else:
    Month = str(month)
year = int(input('enter year: '))

date = Day+'/'+Month+'/'+str(year)
print(date)

# automation

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search/")

# for clicking ok on popup

WebDriverWait(driver, 1000).until(
		 EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button'))
		 ).click()


# for entering input in 'from station' input box

WebDriverWait(driver, 100).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="origin"]/span/input'))
		 ).send_keys(station_from)

# submitting entered input in 'from station' input box
#
# WebDriverWait(driver, 1000).until(
# 		 EC.presence_of_element_located((By.XPATH, '//*[@id="origin"]/span/input'))
# 		 ).send_keys(Keys.ENTER)


# entering the station in ' to station' input box

WebDriverWait(driver, 100).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="destination"]/span/input'))
		 ).send_keys(station_to)


# deleting the pre entered date in "date" input box

WebDriverWait(driver, 1000).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="jDate"]/span/input'))
		 ).send_keys(Keys.CONTROL + 'a')

WebDriverWait(driver, 1000).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="jDate"]/span/input'))
		 ).send_keys(Keys.DELETE)

# entering the date in 'date' input box

WebDriverWait(driver, 100).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="jDate"]/span/input'))
		 ).send_keys(date)

# submitting on after entering date in 'date' input box

WebDriverWait(driver, 1000).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="jDate"]/span/input'))
		 ).send_keys(Keys.ENTER)

# clicking on the search box

WebDriverWait(driver, 100).until(
		 EC.presence_of_element_located((By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button'))
		 ).click()

