import os
import openpyxl

# wb = openpyxl.load_workbook('3000.xlsx')

# sheet = wb['Sheet1']
path = '/Users/main/Desktop/anki/sound-files'
os.chdir(path)
files = os.listdir(path)

for file in files:
    str = file.replace('pronunciation_ru_', '')
    os.rename(file, str)
    print(str)
