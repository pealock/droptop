import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
emailLogin = os.getenv("EMAIL")
passwordLogin = os.getenv("PASSWORD")

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--kiosk")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://droptop-app.com")

driver.find_element("xpath", "//input[@type='email']").send_keys(emailLogin)
driver.find_element("xpath", "//input[@type='password']").send_keys(passwordLogin)
driver.find_element("xpath", "//input[@type='submit']").click()

time.sleep(3)

siteSelect = Select(driver.find_element("xpath","//div/select"))
siteSelect.select_by_index(1)

time.sleep(3)

driver.get("https://droptop-app.com/dash/active_orders?t=fullscreen")

time.sleep(3)


#Force Bayselect Window

baySelectWindow = driver.find_element("xpath", "/html/body/div[1]/div/div[4]/div[2]/div[4]/i")
driver.execute_script("arguments[0].click();", baySelectWindow)
time.sleep(1)

baySelector1 = driver.find_element("xpath", "/html/body/div/div/div[4]/div[2]/div[7]/div/div[2]/div[1]/div[2]/div/label")
driver.execute_script("arguments[0].click();", baySelector1)
baySelector2 = driver.find_element("xpath", "/html/body/div/div/div[4]/div[2]/div[7]/div/div[2]/div[1]/div[3]/div/label")
driver.execute_script("arguments[0].click();", baySelector2)
baySelector3 = driver.find_element("xpath", "/html/body/div/div/div[4]/div[2]/div[7]/div/div[2]/div[1]/div[5]/div/label")
driver.execute_script("arguments[0].click();", baySelector3)

time.sleep(1)

driver.find_element("xpath", "/html/body/div[1]/div/div[4]/div[2]/div[7]/div/div[2]/div[1]/div[6]/button").click()