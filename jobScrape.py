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

topCompaniesInternship = "https://www.linkedin.com/jobs/search/?currentJobId=4132943399&distance=25&f_C=11130470%2C18801275%2C33246798%2C9561%2C75642424%2C85645770%2C1586%2C10891165%2C7602863%2C76595620%2C10464881%2C10799650%2C10981144%2C11046103%2C12955216%2C1441%2C162322%2C1684122%2C18280200%2C18293159%2C19080118%2C19207744%2C2002%2C2003%2C2004%2C20708%2C30846%2C3200474%2C3308308%2C34228736%2C3608%2C38552%2C3959849%2C40018%2C42881474%2C631686%2C6407329%2C737010%2C74736676%2C7584134%2C7952659%2C8296%2C83277441%2C89680213%2C90594574&f_E=1&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

topCompanies = "https://www.linkedin.com/jobs/search/?currentJobId=4149267053&distance=25&f_C=11130470%2C18801275%2C33246798%2C9561%2C75642424%2C85645770%2C1586%2C10891165%2C7602863%2C76595620%2C10464881%2C10799650%2C10981144%2C11046103%2C12955216%2C1441%2C162322%2C1684122%2C18280200%2C18293159%2C19080118%2C19207744%2C2002%2C2003%2C2004%2C20708%2C30846%2C3200474%2C3308308%2C34228736%2C3608%2C38552%2C3959849%2C40018%2C42881474%2C631686%2C6407329%2C737010%2C74736676%2C7584134%2C7952659%2C8296%2C83277441%2C89680213%2C90594574&f_E=2%2C3&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

allInternships = "https://www.linkedin.com/jobs/search/?currentJobId=4146242460&distance=25&f_E=1&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"

highVolumeInternship = "https://www.linkedin.com/jobs/search/?currentJobId=4137105574&distance=25&f_C=30846%2C15564&f_E=1&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"

highVolumeFullTime = "https://www.linkedin.com/jobs/search/?currentJobId=4133212572&distance=25&f_C=30846%2C15564&f_E=2%2C3&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"

allJobs = "https://www.linkedin.com/jobs/search/?currentJobId=4117482708&distance=25&f_E=2%2C3&f_TPR=r2592000&geoId=103644278&keywords=mechanical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"

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
import traceback  # Import traceback for detailed error messages

def harvest(link, type, page, priority):
    """ Extracts job postings from a LinkedIn job search page """

    print(f"\n>>> Starting harvest: {type}, Page: {page}, Priority: {priority}")

    try:
        target_url = link + pageKey[1 - int(page)]
        print(f"Navigating to: {target_url}")
        driver.get(target_url)
        time.sleep(randomWaitTime() * 2)
        print("Successfully loaded webpage.")

        # Scroll to the footer to trigger job listings loading
        print("Scrolling to footer...")
        try:
            footer_element = driver.find_element(By.XPATH, "//footer[contains(@aria-label,'LinkedIn Footer Content')]")
            driver.execute_script("arguments[0].scrollIntoView();", footer_element)
            time.sleep(2)
            print("Scrolled to footer successfully.")
        except Exception as e:
            print(f"Error scrolling to footer: {e}")
            traceback.print_exc()

        # Find job postings
        print("Searching for job postings...")
        jobPostings = driver.find_elements(By.CLASS_NAME, "job-card-container")
        print(f"Found {len(jobPostings)} job postings.")

        if not jobPostings:
            print("No job postings found. Exiting function.")
            return  # Exit early if no jobs are found

        for idx, e in enumerate(jobPostings):
            print(f"\n>>> Processing job {idx + 1}/{len(jobPostings)}")

            try:
                with open("jobs.json") as infile:
                    job_postings_list = json.load(infile)
                    print("Loaded jobs.json successfully.")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading jobs.json: {e}")
                traceback.print_exc()
                job_postings_list = []

            tags = []

            try:
                print("Waiting for job title element to appear...")
                WebDriverWait(e, 10).until(
                    EC.presence_of_element_located((By.XPATH, ".//a[contains(@class, 'job-card-container__link')]"))
                )
                print("Job title element is present. Attempting to click...")

                title_element = e.find_element(By.XPATH, ".//a[contains(@class, 'job-card-container__link')]")
                title_element.click()
                time.sleep(randomWaitTime() * 4)
                print("Successfully clicked on job title.")

            except NoSuchElementException:
                print("ERROR: Could not find job title element for this job. Skipping to next.")
                traceback.print_exc()
                continue  # Skip this job and proceed with the next

            if len(driver.find_elements(By.XPATH, "//span[text()='Easy Apply']")) == 0:
                print("Not an Easy Apply job, proceeding...")
                time.sleep(randomWaitTime())

                jobID = str(uuid.uuid4())

                try:
                    title = e.find_element(By.XPATH, ".//a[contains(@class, 'job-card-container__link')]").text

                    print(f"Job Title: {title}")
                except Exception as e:
                    print(f"Error finding job title: {e}")
                    traceback.print_exc()
                    title = "Mechanical Engineer"

                try:
                    companyName = e.find_element(By.CLASS_NAME, "job-card-container__primary-description").text
                    print(f"Company Name: {companyName}")
                except Exception as e:
                    print(f"Error finding company name: {e}")
                    traceback.print_exc()
                    companyName = "None"

                try:
                    location = e.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
                    print(f"Location: {location}")
                    state = location[-2:]
                    state_name = state_codes_formatted.get(state, "unknown")
                    tags.append(state_name)

                    for t in keyTags:
                        if t.lower() in title.lower():
                            tags.append(t)

                    if "manufacturing" in title.lower() and "manufacturing" not in tags:
                        tags.append("manufacturing")
                    if "product" in title.lower() and "product design" not in tags:
                        tags.append("product design")
                    if "system" in title.lower() and "product design" not in tags:
                        tags.append("product design")
                    if type == "intern" and "internship" not in tags:
                        tags.append("internship")
                    if type == "ft":
                        tags.append("full-time")
                except Exception as e:
                    print(f"Error processing location: {e}")
                    traceback.print_exc()

                try:
                    image = e.find_element(By.XPATH, ".//img[starts-with(@id,'ember')]").get_attribute("src")
                    print(f"Image URL: {image}")
                except Exception as e:
                    print("No image found.")
                    image = ""

                try:
                    posted = driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__posted-date").text
                    print(f"Posted Date: {posted}")
                except Exception as e:
                    print("No posted date found.")
                    posted = ""

                buttons = driver.find_elements(By.CLASS_NAME, "jobs-apply-button")
                print(f"Apply Buttons Found: {len(buttons)}")

                if len(buttons) > 0:
                    try:
                        print("Clicking apply button...")
                        driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
                        time.sleep(randomWaitTime())

                        # Handle modal pop-up
                        if len(driver.find_elements(By.CLASS_NAME, "artdeco-modal-overlay")) > 0:
                            print("Modal detected, closing it...")
                            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
                            time.sleep(randomWaitTime())

                        time.sleep(randomWaitTime() * 2)
                        driver.switch_to.window(driver.window_handles[1])
                        time.sleep(randomWaitTime())

                        applicationURL = driver.current_url.replace('?source=LinkedIn', '') + '?utm_source=job-board&utm_medium=website&utm_campaign=job-listing'
                        print(f"Application URL: {applicationURL}")

                        driver.close()
                        time.sleep(randomWaitTime())
                        driver.switch_to.window(driver.window_handles[0])
                        print("Back to job search.")
                    except Exception as e:
                        print(f"Error handling job application: {e}")
                        traceback.print_exc()
                        applicationURL = "https://www.hardwareishard.net/job-board"
                else:
                    applicationURL = "https://www.hardwareishard.net/job-board"

                job_posting = {
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
                print(f"Job added: {title} at {companyName}")

                with open("jobs.json", "w") as outfile:
                    json.dump(job_postings_list, outfile, indent=4)
                print("Updated jobs.json successfully.")

                time.sleep(randomWaitTime())

        print("Completed processing job postings.")

    except Exception as e:
        print(f"Unexpected error in harvest(): {e}")
        traceback.print_exc()

    try:
        githubUpdates.git_push()
        print("GitHub updated.")
    except Exception as e:
        print(f"Error pushing to GitHub: {e}")
        traceback.print_exc()


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
