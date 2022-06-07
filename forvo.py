from selenium import webdriver
import openpyxl
import selenium.common.exceptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

from forvo_page import ForvoPage


# Test Setup
profile = FirefoxProfile()
profile.set_preference('browser.download.dir', '/Downloads')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference(
    'browser.helperApps.neverAsk.saveToDisk', 'application/audio/mpeg')
browser = webdriver.Firefox(firefox_profile=profile)

# Go to Forvo
forvo_page = ForvoPage(driver=browser)
forvo_page.go('')
browser.maximize_window()
time.sleep(1)
forvo_page.agree_button.click()

# Log in to Forvo
forvo_page.username.input_text('')
forvo_page.password.input_text('')
forvo_page.login_button.click()


# reasearch before modularising
wb = openpyxl.load_workbook('4000.xlsx')
# print(type(wb))
# print(wb.sheetnames)
sheet = wb['Sheet1']

for i in range(2, 9):
    try:
        # forvo_page.keyword_button.click()
        website_link = sheet[f'C{i}'].value
        browser.get(website_link)
        time.sleep(3)
        print(i)
        keyword_pronounciation = forvo_page.pronounciation.text
        sheet[f'B{i}'].value = keyword_pronounciation
        wb.save('4000.xlsx')
    except Exception:
        sheet[f'B{i}'].value = 'no spelling'
        # continue
    try:
        # forvo_page.keyword_button.click()
        forvo_page.download_button.click()
        sheet[f'A{i}'].value = 'sound file downloaded'
    except Exception:
        sheet[f'A{i}'].value = 'no sound file'

wb.save('4000.xlsx')
print("operation finished! press any button to shut the browser down")
# forvo_page.download_button.click()

input()
browser.quit()
