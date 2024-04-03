import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from bayID import bay1, bay2, bay3, bay4
from chromeOptions import options

load_dotenv()
emailLogin = os.getenv("EMAIL")
passwordLogin = os.getenv("PASSWORD")

service = Service(executable_path='/usr/bin/chromedriver')

driver = webdriver.Chrome(service=service,
                          options=options)

wait = WebDriverWait(driver, 10)

driver.get("https://droptop-app.com")

driver.find_element("xpath", "/html/body/div[1]/div/div/div[3]/form/div[1]/input").send_keys(emailLogin)
driver.find_element("xpath", "//input[@type='password']").send_keys(passwordLogin)
driver.find_element("xpath", "//input[@type='submit']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//div/select")))

siteSelect = Select(driver.find_element("xpath","//div/select"))
siteSelect.select_by_index(1)

driver.get("https://droptop-app.com/dash/active_orders?t=fullscreen")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[4]/i")))

baySelectWindow = driver.find_element("xpath", "/html/body/div[1]/div/div[4]/div[2]/div[4]/i")
driver.execute_script("arguments[0].click();", baySelectWindow)

wait.until(EC.presence_of_element_located((By.XPATH, bay1)))

baySelector1 = driver.find_element("xpath", bay2)
driver.execute_script("arguments[0].click();", baySelector1)
baySelector2 = driver.find_element("xpath", bay3)
driver.execute_script("arguments[0].click();", baySelector2)
baySelector3 = driver.find_element("xpath", bay4)
driver.execute_script("arguments[0].click();", baySelector3)

driver.find_element("xpath", "/html/body/div[1]/div/div[4]/div[2]/div[7]/div/div[2]/div[1]/div[6]/button").click()

driver.execute_script("document.body.style.zoom='125%'")
