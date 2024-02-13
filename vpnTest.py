import expressvpn
from expressvpn import wrapper
from expressvpn.wrapper import activation_check
from expressvpn.wrapper import connect
from expressvpn.wrapper import connect_alias
from expressvpn.wrapper import disconnect
from expressvpn.wrapper import random_connect
from expressvpn.commands import *

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
from selenium.common.exceptions import NoSuchElementException


connect_alias("usny")

print("connected")
driver = webdriver.Firefox()
driver.get("https://www.hardwareishard.net/")
