#! python3v
# make_flashcards.py creates cards in anki with help of GUI automation


import openpyxl
import pyperclip
import pyautogui
import time

# load the s/s with keywords that will be used in anki cards
wb = openpyxl.load_workbook('3000.xlsx')
sheet = wb['Sheet1']


time.sleep(1)

# loop over keywords and paste them into the fields

for i in range(901, 931):
    translation = sheet[f'F{i}'].value
    word = sheet[f'D{i}'].value
    gender = sheet[f'E{i}'].value

    ipa = sheet[f'B{i}'].value

    pyautogui.moveTo(65, 155, 0.25)
    pyautogui.click()

    for i in (translation, word, gender, ipa):
        pyperclip.copy(i)
        pyautogui.keyDown('command')
        pyautogui.press('v')
        pyautogui.keyUp('command')

        pyautogui.press('tab')

    pyautogui.moveTo(800, 800, 0.25)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.keyDown('command')
    pyautogui.press('c')
    pyautogui.keyUp('command')

    pyautogui.moveTo(60, 400, 0.25)
    pyautogui.click()
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')

    pyautogui.moveTo(800, 400, 0.25)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.keyDown('command')
    pyautogui.press('c')
    pyautogui.keyUp('command')

    pyautogui.moveTo(60, 450, 0.25)
    pyautogui.click()
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')

    pyautogui.moveTo(115, 880, 0.25)
    pyautogui.click()

# pyautogui.moveTo(752, 211, 0.25)
# prononunciation = sheet[f'C{i}'].value
# pyperclip.copy(prononunciation)
# pyautogui.click()
# pyautogui.keyDown('command')
# pyautogui.press('v')
# pyautogui.keyUp('command')

# # drop sound file into the flashcard
# pyautogui.moveTo(689, 115, 0.25)
# pyautogui.click()
# pyautogui.dragTo(1408, 209, 0.25, button="left")
# pyautogui.click()

# # move to add button and press it
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')

# # remove the sound file
# pyautogui.moveTo(689, 115, 0.25)
# pyautogui.click(button="right")
# pyautogui.moveTo(720, 180, 0.25)
# pyautogui.click()
