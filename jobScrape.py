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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options



pageKey = ["","&start=25","&start=50","&start=75","&start=100"]
current_page = 1
jobSearch = "Mechanical Engineering Internship"
searchDestination = "United States"
Email = "Kate19Anderson2001@gmail.com"
Password = "Ryobi&Dewault"
pages = ["1","2","3","4","5"]

#########      LINKS    #######

topCompaniesInternship = "https://www.linkedin.com/jobs/search/?currentJobId=3627109309&f_C=19088148%2C3608%2C90594574%2C76595620%2C19207744%2C631686%2C8296%2C80086817%2C162322%2C74903048%2C81668991%2C737010%2C18203768%2C10891165%2C18293159%2C3959849%2C7952659%2C7602863%2C1586%2C18801275%2C2706887%2C2734%2C3308308%2C10464881%2C10799650%2C10981144%2C11046103%2C12587763%2C12955216%2C1384%2C1412%2C1441%2C1472%2C1483%2C1684122%2C18067251%2C18157704%2C18238200%2C18264661%2C18280200%2C1882%2C1904%2C1999%2C2002%2C2003%2C2004%2C20708%2C27238745%2C30846%2C3200474%2C34228736%2C3591568%2C40018%2C42881474%2C51607174%2C5383634%2C5770%2C6407329%2C7584134%2C7939313%2C83277441&f_E=1&f_TPR=r2592000&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

topCompanies = "https://www.linkedin.com/jobs/search/?currentJobId=3560522221&f_C=1586%2C1384%2C18264661%2C11046103%2C83277441%2C1904%2C5383634%2C3200474%2C18293159%2C3308308%2C3591568%2C10799650%2C7602863%2C51607174%2C5770%2C18280200%2C18067251%2C3959849%2C1412%2C10464881%2C1684122%2C6407329%2C1882%2C2734%2C1441%2C42881474%2C18203768%2C18157704%2C7952659%2C27238745%2C20708%2C7939313%2C18238200%2C12587763%2C1472%2C10981144%2C7584134%2C34228736%2C40018%2C10891165%2C18801275%2C2706887%2C12955216%2C1999%2C737010%2C2002%2C2003%2C1116%2C2004&f_E=2%2C3&f_TPR=r2592000&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true&sortBy=R"

allInternships = "https://www.linkedin.com/jobs/search/?currentJobId=3459209529&f_E=1&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering%20Internship&location=United%20States&refresh=true"

highVolumeInternship = "https://www.linkedin.com/jobs/search/?currentJobId=3675774051&f_C=15564%2C1319%2C1344%2C2018%2C1116&f_E=1&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true&sortBy=R"

highVolumeFullTime = "https://www.linkedin.com/jobs/search/?currentJobId=3473956093&f_C=30846%2C1483%2C2018%2C1344%2C1319%2C15564&f_E=2%2C3&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true&sortBy=R"
allJobs = "https://www.linkedin.com/jobs/search/?currentJobId=3483542671&f_E=2%2C3&f_TPR=r604800&geoId=103644278&keywords=Mechanical%20Engineering&location=United%20States&refresh=true"

state_codes = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}
state_codes_formatted = {code: name.lower().replace(' ', '-') for code, name in state_codes.items()}

keyTags = ["co-op","internship","manufacturing","autodesk inventor","finite element analysis (fea)","catia","computer-aided design (cad)","composites","aerodynamics", "Geometric Dimensioning & Tolerancing"," Tooling Design ","ITAR"]

linkedInLogin = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
# One-line dictionary comprehension to format the dictionary



def randomWaitTime():
    r1 = random.randint(1, 4)
    return r1


# Path to geckodriver executable
geckodriver_path = '/usr/local/bin/geckodriver'

# Create a Service object
service = Service(geckodriver_path)
print("in options section")
# Configure Firefox options
options = Options()
options.set_preference('fission.bfcacheInParent', False)
options.set_preference('fission.webContentIsolationStrategy', 0)
#options.add_argument('-headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
print("exited options")
# Initialize the Firefox webdriver with the Service object and options
try:
    driver = webdriver.Firefox(service=service, options=options)
    print("assigned driver")
except Exception as e:
    print("Error creating webdriver:", e)
print("assigned driver")
driver.get(linkedInLogin)
print("on login page)")
element = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.ID, "username")))
time.sleep(randomWaitTime())
driver.save_screenshot('screenshot.png')
email = driver.find_element(By.ID, "username")
print("found username")
email.clear()
time.sleep(randomWaitTime())
email.send_keys("Kate19Anderson2001@gmail.com")
driver.save_screenshot('screenshot1.png')
time.sleep(randomWaitTime())

password = driver.find_element(By.ID, "password")
print("found password")
password.clear()
time.sleep(randomWaitTime())
password.send_keys("Ryobi&Dewault")
time.sleep(randomWaitTime())
password.send_keys(Keys.RETURN)
time.sleep(randomWaitTime()*3)
print("logged in")


## FUNCTIONS
def harvest(link,type,page,priority):
    driver.get(link + pageKey[1 - int(page)])
    time.sleep(randomWaitTime()*2)
    print("made to webpage")
    #driver.execute_script("document.body.style.zoom='30%'")
    #print("zoomed")
    time.sleep(randomWaitTime())
#    element = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Page')]")
    element = driver.find_element(By.XPATH, "//footer[contains(@aria-label,'LinkedIn Footer Content')]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)
    try:
        jobPostings = driver.find_elements(By.CLASS_NAME,"job-card-container")
        print(len(jobPostings))
        print("job postings found")

        for e in jobPostings:

            try:
                with open("jobs.json") as infile:
                    job_postings_list = json.load(infile)
            except (FileNotFoundError):
                print("jobs json load issue")
                pass
            tags = []
            title = e.find_element(By.CLASS_NAME,"job-card-list__title").click()
            time.sleep(randomWaitTime()*4)
            if len(driver.find_elements(By.XPATH, "//span[text()='Easy Apply']")) == 0:
                time.sleep(randomWaitTime())
                jobID = str(uuid.uuid4())

                try:
                    title = e.find_element(By.CLASS_NAME,"job-card-list__title")
                    title = title.text
                except Exception:
                    title = "Mechanical Engineer"
                try:
                    companyName = e.find_element(By.CLASS_NAME, "job-card-container__primary-description") #  OLD: job-card-container__company-name
                    companyName = companyName.text
                except Exception:
                    companyName = "None"
                try:
                    location = e.find_element(By.CLASS_NAME,"job-card-container__metadata-item")
                    location = location.text
                    state = location[-2:]
                    state_name = state_codes_formatted.get(state)
                    tags.append(state_name)
                    for t in keyTags:
                        if t in title.lower():
                            tags.append(t)
                    if "manufacturing" in title.lower() and "manufacturing" not in tags:
                        tags.append("manufacturing")
                    if "product" in title.lower() and "product design" not in tags:
                        tags.append("product design")
                    if "system" in title.lower() and "product design" not in tags:
                        tags.append("product design")
                    if type == "intern" and "internship" not in tags:
                        tags.append("internship")
                    if type == ("ft"):
                        tags.append("full-time")
                except Exception:
                    print("no location")
                try:
                    image = e.find_element(By.XPATH, ".//img[starts-with(@id,'ember')]")
                    image = image.get_attribute("src")
                except Exception:
                    print("no image")
                try:
                    posted = driver.find_element(By.CLASS_NAME,"jobs-unified-top-card__posted-date")
                    posted = posted.text
                except:
                    print("no post date")
                    posted = ""
                buttons = driver.find_elements(By.CLASS_NAME,"jobs-apply-button")
                #print(buttons)
                if len(buttons) > 0:
                    #print("got url")
                    apply = driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()
                    time.sleep(randomWaitTime())
                    if len(driver.find_elements(By.CLASS_NAME, "artdeco-modal-overlay.artdeco-modal-overlay--layer-default.artdeco-modal-overlay--is-top-layer.display-flexflex-column justify-center.ember-view")) > 0:
                        exit = driver.find_element(By.CLASS_NAME,"artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view artdeco-modal__dismiss").click()
                        time.sleep(randomWaitTime())
                        apply = driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()


                    time.sleep(randomWaitTime()*2)
                    #continueAgain = driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()
                    time.sleep(randomWaitTime())
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(randomWaitTime())
                    applicationURL = driver.current_url
                    applicationURL = applicationURL.replace('?source=LinkedIn', '')
                    applicationURL += '?utm_source=job-board&utm_medium=website&utm_campaign=job-listing'
                    print("got url")
                    driver.close()
                    time.sleep(randomWaitTime())
                    driver.switch_to.window(driver.window_handles[0])
                    print("back to search")
                    time.sleep(randomWaitTime())
                else:
                    applicationURL = "https://www.hardwareishard.net/job-board"

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
                print("list appended")
                with open("jobs.json", "w") as outfile:
                    json.dump(job_postings_list,outfile)
                print("json dumped")
                time.sleep(randomWaitTime())
            #    print(job_postings_list)
            #    time.sleep(randomWaitTime())
            #    with open("jobs.json", "r") as outfile:
            #        sorted_job_list = sorted(job_postings_list, key=lambda x: int(x["priority"]))
            #    with open("jobs.json", "w") as outfile:
            #        json.dump(sorted_job_list, outfile)
                print("a job collection has completed")
    except:
        print("no more job postings for this search")
        pass
    githubUpdates.git_push()
    print("github updated")


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
def delete_duplicate_entries():
    with open("jobs.json", "r") as infile:
        job_postings_list = json.load(infile)

    unique_job_postings = []
    titles = set()

    for job in job_postings_list:
        if job['title'] not in titles:
            unique_job_postings.append(job)
            titles.add(job['title'])

    with open("jobs.json", "w") as outfile:
        json.dump(unique_job_postings, outfile)
def delete_jobs_by_priority(priority):
    try:
        # Load the JSON data
        with open('jobs.json', 'r') as file:
            job_postings_list = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return

    # Filter out entries with the specified priority
    filtered_job_postings = [job for job in job_postings_list if job['priority'] != priority]

    # Write the filtered list back to the JSON file
    with open('jobs.json', 'w') as file:
        json.dump(filtered_job_postings, file)


###### LIVE CODE #################

delete_jobs_by_priority(0)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(topCompaniesInternship,"intern",p,0)
shuffle()
print("harvested top internships")

delete_jobs_by_priority(1)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(highVolumeInternship,"intern",p,1)
shuffle()
print("harvested high volume internships")

delete_jobs_by_priority(2)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(topCompanies,"ft",p,2)
shuffle()
print("harvested top companies")

delete_jobs_by_priority(3)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(highVolumeFullTime,"ft",p,3)
shuffle()
print("harvested high volume companies")

delete_jobs_by_priority(4)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(allInternships,"intern",p,4)
shuffle()
print("harvested all internships")

delete_jobs_by_priority(5)
for p in pages:
    time.sleep(randomWaitTime())
    harvest(allJobs,"ft",p,5)
shuffle()
print("harvested all jobs")
delete_duplicate_entries()
