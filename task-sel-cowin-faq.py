# Using Python Selenium and the URL https://www.cowin.gov.in/ you have to :-
# 1) click on the "Create "FAQ" and "Partners" anchor tags present on the Home page and open two new windows.
# 2) Now, you have to fetch the opened Windows / Frame ID and display the same on the console.
# 3) Kindly close the two new windows and come back to the Home page also.

import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cowin.gov.in/")

#FAQ rightclick open in new window
faq_link=driver.find_element(By.XPATH,"//a[text()=' FAQ ']")
faq_url=faq_link.get_attribute('href')
faq_link.click()
time.sleep(4)

#partner
partner_link=driver.find_element(By.XPATH,"//a[text()=' Partners ']")
partner_url = partner_link.get_attribute('href')
partner_link.click()
time.sleep(4)

window_handles=driver.window_handles
#display window handles in console
print("window handles of opened windows")
for handle in window_handles:
    print(handle)

#close the opened windows
main_window_handle=driver.current_window_handle
for handle in window_handles:
    if handle !=main_window_handle:
        driver.switch_to.window(handle)
        driver.close()
time.sleep(4)
#switch to main window
driver.switch_to.window(main_window_handle)

driver.get("https://cowin.gov.in/")
driver.quit()

