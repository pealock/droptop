from selenium.webdriver.chrome.options import Options

prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option("prefs", prefs)
options.add_argument("--kiosk")