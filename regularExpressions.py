# импорт функций использующие регулярные выражения
import re
from datetime import datetime
from dateutil.parser import parse

regExp1 = r'\d{3}'  # поиск трехзначных чисел
regExp2 = r'(?:^|(?<=\s))\w{3}(?=\s|$)'  # поиск набора из трех символов
regExp3 = r'(\.)'  # поиск точки
regExp4 = r'[0-9]{1}/[0-9]{2}/[0-9]{4}|[0-9]{2}.[0-9]{2}.[0-9]{4}'  # нахождение даты формата dd/mm/yyyy dd.mm.yyyy
clearOut = []
rawOut = []
# замена набора символов из трех букв на словосочетание Регулярное выражение

with open('randomText.txt', newline="", encoding='utf-8') as openFile:
    with open('outputFile1.txt', 'wt', encoding='utf-8') as outputFile:
        for line in openFile:
            outputFile.write(re.sub(regExp2, 'Регулярное выражение', line))

# замена точки на ',!'

with open('randomText.txt', newline="", encoding='utf-8') as openFile:
    with open('outputFile2.txt', 'wt', encoding='utf-8') as outputFile:
        for line in openFile:
            outputFile.write(re.sub(regExp3, ',!', line))

# поиск трехзначных последовательностей чисел и складывание их в массив

with open('randomSymbols.txt', newline="", encoding='utf-8') as openFile:
    with open('outputFile3.txt', 'wt', encoding='utf-8') as outputFile:
        patter = re.compile(regExp1)
        for line in openFile:
            rawOut = (re.findall(regExp1, line))
            for i in rawOut:
                if int(i) >= 0:
                    clearOut.append(i)
    print(clearOut)

date_input = input('Enter a date(mm/dd/yyyy): ')
correctDate = str(parse(date_input))
correctDate = correctDate.split()
print(correctDate[0])
date_object = datetime.strptime(correctDate[0], '%Y-%m-%d')
print(date_object)
