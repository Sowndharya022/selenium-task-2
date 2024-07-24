# Using Python Selenium visit the URL https://labour.gov.in/
# Goto the Menu whose name is "Media" where you will find a sub-menu whose name is "Photo Gallery". Your task is to
# download the 10 photos from the webpage and store them in a folder. Kindly create the folder using Python only
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

download_dir = os.path.join(os.getcwd(), "PhotoGallery")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


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

try:
    media_menu=driver.find_element(By.XPATH,"//a[normalize-space()='Media']")
    media_menu.click()
    more_info = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Click for more info of Press Releases']"))
    )
    more_info.click()
    photo = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Photo Gallery'])[2]"))
    )
    time.sleep(3)
    href=photo.get_attribute('href')
    driver.get(href)
    time.sleep(4)

    window_after=driver.window_handles[0]

    #Fetch image elements
    image_elements=driver.find_elements(By.XPATH,"//table//img")
    #fetch urls
    image_urls=[element.get_attribute('src')for element in image_elements[:10]]
    for i,url in enumerate(image_urls,1):
        try:
            response=requests.get(url)
            if response.status_code==200:
                with open(os.path.join(download_dir,f"image_(i).jpeg"),"wb")as f:
                    f.write(response.content)
                    print(f"downloaded image{i}")
            else:
                print(f"failed to download image {i}")
        except Exception as e:
            print(f"Error occurred while downloading image {i}: {str(e)}")


except Exception as e:
    print(f"An error occurred: {str(e)}")


finally:
    driver.quit()