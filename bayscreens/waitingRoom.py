import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from bayID import bay1, bay2, bay3, bay4
from chromeOptions import options

load_dotenv()
emailLogin = os.getenv("EMAIL")
passwordLogin = os.getenv("PASSWORD")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

wait = WebDriverWait(driver, 10)

driver.get("https://droptop-app.com")

driver.find_element("xpath", "//input[@type='email']").send_keys(emailLogin)
driver.find_element("xpath", "//input[@type='password']").send_keys(passwordLogin)
driver.find_element("xpath", "//input[@type='submit']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//div/select")))

siteSelect = Select(driver.find_element("xpath","//div/select"))
siteSelect.select_by_index(1)

driver.get("https://droptop-app.com/dash/active_orders?t=fullscreen")