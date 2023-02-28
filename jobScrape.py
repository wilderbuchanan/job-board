from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
import githubUpdates


jobSearch = "Mechanical Engineering Internship"
searchDestination = "United States"
Email = "Kate19Anderson2001@gmail.com"
Password = "Ryobi&Dewault"

topCompaniesInternship = "https://www.linkedin.com/jobs/search/?currentJobId=3495954434&f_C=10464881%2C1684122%2C1586%2C2018%2C6407329%2C42881474%2C1441%2C1384%2C1483%2C18264661%2C18203768%2C18157704%2C11046103%2C83277441%2C7952659%2C27238745%2C1904%2C5383634%2C18293159%2C7939313%2C18238200%2C12587763%2C1472%2C10981144%2C7584134%2C34228736%2C40018%2C18801275%2C10799650%2C7602863%2C51607174%2C18280200%2C30846%2C18067251%2C12955216%2C1999%2C737010%2C2002%2C2003%2C1116%2C2004%2C1412%2C3959849%2C15564&f_E=1&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true&sortBy=R&start=25"

topCompanies = "https://www.linkedin.com/jobs/search/?currentJobId=3407862076&f_C=10464881%2C1684122%2C1586%2C2018%2C6407329%2C42881474%2C1441%2C1384%2C1483%2C18264661%2C18203768%2C18157704%2C11046103%2C83277441%2C7952659%2C27238745%2C1904%2C5383634%2C18293159%2C7939313%2C18238200%2C12587763%2C1472%2C10981144%2C7584134%2C34228736%2C40018%2C18801275%2C10799650%2C7602863%2C51607174%2C18280200%2C30846%2C18067251%2C12955216%2C1999%2C737010%2C2002%2C2003%2C1116%2C2004%2C1412%2C3959849%2C15564&f_E=2%2C3&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true&sortBy=R"

allJobs = "https://www.linkedin.com/jobs/search/?currentJobId=3459209529&f_E=1&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering%20Internship&location=United%20States&refresh=true"


state_codes = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}
state_codes_formatted = {code: name.lower().replace(' ', '-') for code, name in state_codes.items()}

keyTags = ["co-op","internship","manufactuing","autodesk inventor","finite element analysis (fea)","catia","computer-aided design (cad)","composites","aerodynamics", "Geometric Dimensioning & Tolerancing"," Tooling Design ","ITAR"]

linkedInLogin = ("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
# One-line dictionary comprehension to format the dictionary

pages = ["1","2","3","4","5"]

def randomWaitTime():
    r1 = random.randint(2, 5)
    return r1

driver = webdriver.Firefox()
driver.get(linkedInLogin)
element = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.ID, "username")))
time.sleep(randomWaitTime())

email = driver.find_element(By.ID, "username")
email.clear()
email.send_keys(Email)
time.sleep(randomWaitTime())

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys(Password)
time.sleep(randomWaitTime())
password.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.ID, "main")))
time.sleep(randomWaitTime()*2)
print("Home")


def harvest(link,page,priority): #0 = top of page
    driver.get(link)
    time.sleep(randomWaitTime()*2)
    driver.execute_script("document.body.style.zoom='30%'")
    time.sleep(randomWaitTime())
#    element = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Page')]")
    element = driver.find_element(By.XPATH, "//footer[contains(@aria-label,'LinkedIn Footer Content')]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)
    jobPostings = driver.find_elements(By.CLASS_NAME,"job-card-container")
    print("found postings")
    job_postings_list = []
    if page == 1:
        with open("jobs.json") as infile:
            job_postings_list = json.load(infile)
        job_postings_list = [job for job in job_postings_list if job['priority'] != priority]
        with open("jobs.json", "w") as outfile:
            json.dump(job_postings_list, outfile)

    for e in jobPostings:

        try:
            with open("jobs.json") as infile:
                job_postings_list = json.load(infile)
        except (FileNotFoundError):
            pass
        tags = []
        title = e.find_element(By.CLASS_NAME,"job-card-list__title").click()
        if len(driver.find_elements(By.XPATH, "//span[text()='Easy Apply']")) == 0:
            time.sleep(randomWaitTime())
            jobID = str(uuid.uuid4())
            title = e.find_element(By.CLASS_NAME,"job-card-list__title")
            title = title.text
            companyName = e.find_element(By.CLASS_NAME, "job-card-container__company-name")
            companyName = companyName.text
            location = e.find_element(By.CLASS_NAME,"job-card-container__metadata-item")
            location = location.text
            state = location[-2:]
            state_name = state_codes_formatted.get(state)
            tags.append(state_name)
            for t in keyTags:
                if t in title.lower():
                    tags.append(t)
            if "intern" in title.lower() and "internship" not in tags:
                tags.append("internship")
            image = e.find_element(By.XPATH, ".//img[starts-with(@id,'ember')]")
            image = image.get_attribute("src")
            posted = driver.find_element(By.CLASS_NAME,"jobs-unified-top-card__posted-date")
            posted = posted.text
            apply = driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()
            time.sleep(randomWaitTime())
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randomWaitTime())
            applicationURL = driver.current_url
            applicationURL += '?utm_source=job-board&utm_medium=website&utm_campaign=job-listing'
            driver.close()
            time.sleep(randomWaitTime())
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(randomWaitTime())
            if len(driver.find_elements(By.XPATH, "//button[contains(@aria-label,'strong')]"))>0:
                skills = driver.find_element(By.XPATH, "//button[contains(@aria-label,'strong')]").click()
                time.sleep(randomWaitTime())
                #caps = driver.find_elements(By.CLASS_NAME, "job-details-skill-match-status-list__unmatched-skill text-body-small")
                caps = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'Your')]")
                for s in caps:
                    cappy = s.text
                    if cappy.lower() in keyTags:
                        tags.append(cappy.lower())
                time.sleep(randomWaitTime())
                close = driver.find_element(By.XPATH, "//span[text()='Done']")
                parent = close.find_element(By.XPATH, "..")
                parent.click()
            time.sleep(randomWaitTime())
            testTittle = title.split()

            job_posting ={
                    "title": title,
                    "company": companyName,
                    "location": location,
                    "applicationURL": applicationURL,
                    "postedDate": posted,
                    "imageURL": image,
                    "tags": tags,
                    "priority": priority
                }
            job_postings_list.append(job_posting)
            with open("jobs.json", "w") as outfile:
                json.dump(job_postings_list,outfile)
            time.sleep(randomWaitTime())
            #print(job_postings_list)
            time.sleep(randomWaitTime())
            with open("jobs.json", "r") as outfile:
                sorted_job_list = sorted(job_postings_list, key=lambda x: int(x["priority"]))
            with open("jobs.json", "w") as outfile:
                json.dump(sorted_job_list, outfile)
    githubUpdates.git_push()
    if page != 0:
        element = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Page " + str(page) + "')]").click()
    time.sleep(randomWaitTime()*2)

def shuffle():
    # Load the JSON data
    with open('jobs.json', 'r') as f:
        data = json.load(f)

    # Group the data by priority level
    grouped_data = {}
    for item in data:
        priority = item['priority']
        if priority not in grouped_data:
            grouped_data[priority] = []
        grouped_data[priority].append(item)

    # Shuffle the data within each priority level
    for priority in grouped_data:
        random.shuffle(grouped_data[priority])

    # Flatten the data back into a list, sorted by priority
    sorted_data = []
    for priority in sorted(map(int, grouped_data.keys())):
        sorted_data += grouped_data[priority]
    with open('jobs.json', 'w') as f:
        json.dump(sorted_data, f)
    # Print the sorted and shuffled data
    #print(sorted_data)


harvest(topCompaniesInternship,1,0)
shuffle()
time.sleep(randomWaitTime())
harvest(topCompaniesInternship,2,0)
shuffle()
time.sleep(randomWaitTime())
for page in pages:
    harvest(topCompanies,page,1)
shuffle()
time.sleep(randomWaitTime())
for page in pages:
    harvest(allJobs,page,2)
shuffle()
