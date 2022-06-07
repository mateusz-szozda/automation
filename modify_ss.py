import openpyxl

wb = openpyxl.load_workbook('4000.xlsx')
sheet = wb['Sheet1']


for i in range(2, 1003):
    old_value = (sheet.cell(row=i, column=1).value)
    keyword = sheet[f'D{i}'].value
    new_value = f"https://yandex.ru/images/search?text={keyword}"
    # new_value = f"https://forvo.com/word/{keyword}/#ru"
    print(new_value)
    # sheet[f'C{i}'].value = new_value
    sheet[f'G{i}'].value = new_value


wb.save('4000.xlsx')
