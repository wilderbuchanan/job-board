from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
from csv import writer
import sys
import uuid
import json

jobSearch = "Mechanical Engineering Internship"

Email = "Kate19Anderson2001@gmail.com"
Password = "Ryobi&Dewault"

link = "https://www.indeed.com/jobs?q=mechanical+engineering+internship"
def randomWaitTime():
    r1 = random.randint(3, 7)
    return r1

driver = webdriver.Firefox()
driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Dmechanical%2Bengineering%2Binternship%26fromage%3D7%26grpKey%3D8gcGdG5mdGNsuA%252BO9AWqECAKCW5vcm10aXRsZRoTbWVjaGFuaWNhbCBlbmdpbmVlcg%253D%253D&tmpl=desktop&service=mob&from=gnav-util-jobsearch--indeedmobile&jsContinue=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Dmechanical+engineering+internship%26fromage%3D7%26grpKey%3D8gcGdG5mdGNsuA%252BO9AWqECAKCW5vcm10aXRsZRoTbWVjaGFuaWNhbCBlbmdpbmVlcg%253D%253D&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.245189569.576253307.1677128838-409744797.1677128838")
time.sleep(randomWaitTime())

email = driver.find_element(By.ID, "ifl-InputFormField-3")
email.clear()
email.send_keys(Email)
time.sleep(randomWaitTime())
if len(rightPanel.find_elements(By.XPATH, "//a[starts-with(@class,'css')]"))>0:
    user_input = input("Please enter some input when done ")
email.send_keys(Keys.RETURN)

print("check fo recaptcha")
time.sleep(20)
time.sleep(randomWaitTime())

logIn = driver.find_element(By.ID, "auth-page-google-password-fallback").click()


password = driver.find_element(By.XPATH, "//input[starts-with(@id,'ifl')]")
password.clear()
time.sleep(randomWaitTime())
password.send_keys(Password)
time.sleep(randomWaitTime())
if len(rightPanel.find_elements(By.XPATH, "//a[starts-with(@class,'css')]"))>0:
    user_input = input("Please enter some input when done ")
password.send_keys(Keys.RETURN)

time.sleep(randomWaitTime())

if len(driver.find_elements(By.ID,"verification_input"))>0:
    print("verification needed")
    user_input = input("Please enter some input when done ")
    time.sleep(randomWaitTime())

discover = driver.find_element(By.ID, "FindJobs").click()

what = driver.find_element(By.ID, "text-input-what")
email.clear()
email.send_keys(jobSearch)
time.sleep(randomWaitTime())
email.send_keys(Keys.RETURN)
time.sleep(randomWaitTime())

jobDict = {}

jobPostings = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
time.sleep(randomWaitTime())
print("found job postings")
for e in jobPostings:
    time.sleep(randomWaitTime())
    print("in job posting")
    jobID = str(uuid.uuid4())
    title = e.find_element(By.XPATH, "//span[starts-with(@id,'jobTitle')]")
    print("found title")
    title = title.get_attribute("title")
    print(title)
    companyName = e.find_element(By.CLASS_NAME,"companyName")
    companyName = companyName.text
    print(companyName)
    location = e.find_element(By.CLASS_NAME,"companyLocation")
    location = location.text
    print(location)

    #posting = e.find_element(By.XPATH, "//a[starts-with(@aria-label,'full')]").click()
    posting = e.find_element(By.CLASS_NAME, "resultContent").click()
    time.sleep(randomWaitTime())

    rightPanel = driver.find_element(By.CLASS_NAME,"jobsearch-RightPane")

    if len(rightPanel.find_elements(By.XPATH, "//a[starts-with(@class,'css')]"))>0:
        appURL = driver.find_element(By.XPATH, "//a[starts-with(@class,'css')]").click()
        time.sleep(randomWaitTime())
        print("clicked job")
        driver.switch_to.window(driver.window_handles[1])
        print("switched windows")
        time.sleep(randomWaitTime())
        appURL = driver.find_element(By.XPATH, "//a[starts-with(@class,'css')]").click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(randomWaitTime())
        appURL = driver.current_url
        time.sleep(randomWaitTime())
        driver.close()
        time.sleep(randomWaitTime())

        driver.close()


driver.close()
driver.close()
