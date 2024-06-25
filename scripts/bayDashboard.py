import os
import sys
import socket
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from bayID import bay1, bay2, bay3, bay4
from chromeOptions import options



# Load Creds
load_dotenv()
emailLogin = os.getenv("EMAIL")
passwordLogin = os.getenv("PASSWORD")

# Define targets
emailForm = "/html/body/div[1]/div/div/div[3]/form/div[1]/input"
baySelect = "/html/body/div[1]/div/div[4]/div/div[2]/i[1]"
baySelectConfirm = "/html/body/div[1]/div/div[4]/div/div[7]/div/div[2]/div[1]/div[6]/button"

# Load webdriver
if 'linux' in sys.platform:
    service = Service(executable_path='/usr/bin/chromedriver')
else:
    service = Service()

# Define driver
driver = webdriver.Chrome(service=service,
                          options=options)
# Define timeout
wait = WebDriverWait(driver, 10)

# Initial website pull
driver.get("https://droptop-app.com")

time.sleep(3)

# Login flow
driver.find_element("xpath", emailForm).send_keys(emailLogin)
driver.find_element("xpath", "//input[@type='password']").send_keys(passwordLogin)
driver.find_element("xpath", "//input[@type='submit']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//div/select")))

# Site select
siteSelect = Select(driver.find_element("xpath", "//div/select"))
siteSelect.select_by_index(1)

# Dashboard Fullscreen
driver.get("https://droptop-app.com/dash/active_orders?t=fullscreen")
wait.until(EC.presence_of_element_located((By.XPATH, baySelect)))

# Bay Selection
baySelectWindow = driver.find_element("xpath", baySelect)
driver.execute_script("arguments[0].click();", baySelectWindow)
wait.until(EC.presence_of_element_located((By.XPATH, bay1)))

# Define Bay Deselects
bayDeselect1 = driver.find_element("xpath", bay1)
bayDeselect2 = driver.find_element("xpath", bay2)
bayDeselect3 = driver.find_element("xpath", bay3)
bayDeselect4 = driver.find_element("xpath", bay4)

# Deselect unused bays depending on hostname

# Bay 1
if "bay1" in socket.gethostname():
    driver.execute_script("arguments[0].click();", bayDeselect2)
    driver.execute_script("arguments[0].click();", bayDeselect3)
    driver.execute_script("arguments[0].click();", bayDeselect4)

# Bay 2
if "bay2" in socket.gethostname():
    driver.execute_script("arguments[0].click();", bayDeselect1)
    driver.execute_script("arguments[0].click();", bayDeselect3)
    driver.execute_script("arguments[0].click();", bayDeselect4)

# Bay 3
if "bay3" in socket.gethostname():
    driver.execute_script("arguments[0].click();", bayDeselect1)
    driver.execute_script("arguments[0].click();", bayDeselect2)
    driver.execute_script("arguments[0].click();", bayDeselect4)

# Bay 4
if "bay4" in socket.gethostname():
    driver.execute_script("arguments[0].click();", bayDeselect1)
    driver.execute_script("arguments[0].click();", bayDeselect2)
    driver.execute_script("arguments[0].click();", bayDeselect3)


# Click submit
driver.find_element("xpath", baySelectConfirm).click()

# Zoom In
driver.execute_script("document.body.style.zoom = '1.25'")

