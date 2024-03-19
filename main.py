from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time

options = webdriver.ChromeOptions()
prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

Browser = webdriver.Chrome(service=Service("/snap/bin/chromium.chromedriver"), options=options)

Browser.get("https://humanbenchmark.com/tests/verbal-memory")

Browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[4]/button").click()

Seen = set()

for count in range(1000):
	element = Browser.find_element(By.CLASS_NAME, "word")
	word = element.text
	print(word)
	if(word in Seen):
		Browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button[1]").click()
	else:
		Seen.add(word)
		Browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button[2]").click()

time.sleep(30)