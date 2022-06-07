from selenium import webdriver
import openpyxl
import selenium.common.exceptions

from forvo_page import ForvoPage

# Test Setup
browser = webdriver.Firefox()
browser.maximize_window()


# get links from excel and open 30 tabs with links from excel
wb = openpyxl.load_workbook('4000.xlsx')
sheet = wb['Sheet1']
# browser.get('https://duckduckgo.com/?t=ffab&q=test&iax=images&ia=images')

for i in range(591, 601):
    website_link = sheet[f'G{i}'].value
    browser.execute_script(
        f'window.open("{website_link}","_blank");')
