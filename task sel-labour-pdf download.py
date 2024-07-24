# Using Python Selenium visit the URL https://labour.gov.in/ and do the following tasks given below:-
# Goto the Menu whose name is "Documents" and Download the Monthly Progress Report.

import os
import shutil
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#set download directory
cd=os.getcwd()
download_dir=cd+"\\Notes\\"
if os.path.exists(download_dir):
    shutil.rmtree(download_dir)
else:
    os.mkdir(download_dir)

#setting options for chrome
chrome_options=Options()
chrome_options.add_experimental_option("prefs",{"plugins.always_open_pdf_externally":True,
    "download.default_directory":download_dir,
    "download.prompt_for_download":False,
    "download.directory_upgrade":True,
    "safebrowsing.enabled":True})
chrome_options.add_argument("--safebrowsing-disable-download-protection")
chrome_options.add_argument("safebrowsing-disable-extension-blacklist")

#Initialize chrome with options
driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()

#open website
driver.get("https://labour.gov.in/ ")

#click monthly reports
try:
    act=ActionChains(driver)
    documents=driver.find_element(By.XPATH,"//a[normalize-space()='Documents']")
    #hover over the element
    act.move_to_element(documents).perform()
    monthly_progress_link=WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Monthly Progress Report")]')))
    monthly_progress_link.click()
    download_link=WebDriverWait(driver,23).until(EC.element_to_be_clickable((By.XPATH,'//td[contains(text(),"January-2024")]/following::a[1]')))
    download_link.click()

    time.sleep(3)

    #click
    pyautogui.press('enter')
    time.sleep(2)
except TimeoutException:
    print("timeout exception")


    driver.quit()



