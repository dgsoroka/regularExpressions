# импорт функций использующие регулярные выражения
import re

regExp1 = r'\b\w{5}\b'  # поиск 5-и буквенных слов
regExp2 = r'(?:^|(?<=\s))\w{3}(?=\s|$)'  # поиск набора из трех символов
regExp3 = r'.'  # поиск точки
regExp4 = r'[0-9]{1}/[0-9]{2}/[0-9]{4}|[0-9]{2}.[0-9]{2}.[0-9]{4}'  # нахождение даты формата dd/mm/yyyy dd.mm.yyyy
regExp5 = r'/'
clearOut = []
rawOut = []
# замена набора символов из трех букв на словосочетание Регулярное выражение

with open('randomText.txt', newline="", encoding='utf-8') as openFile:
    with open('outputFile1.txt', 'wt', encoding='utf-8') as outputFile:
        for line in openFile:
            outputFile.write(re.sub(regExp2, 'Регулярное выражение', line))

# замена точки на 'заменаТочки'

with open('text.txt', newline="", encoding='utf-8') as openFile:
    with open('output2.txt', 'wt', encoding='utf-8') as outputFile:
        for line in openFile:
            outputFile.write(re.sub(regExp3, 'заменаТочки', line))

# поиск слов с 5 буквами и замена на 'пятибуквенное слово'

with open('text.txt', newline="", encoding='utf-8') as openFile:
    with open('output3.txt', 'wt', encoding='utf-8') as outputFile:
        patter = re.compile(regExp1)
        for line in openFile:
            outputFile.write(re.sub(regExp1, 'пятибуквенное слово', line))

# заменям точку на запятую в веденном числе

numWithDot = input('Введите число с точкой ')
numWithComma = re.sub(regExp3, ',', numWithDot)
print(f'В вашем числе исправлена точка: {numWithComma}')

# исправляем дату

date_input = input('Enter a date(dd/mm/yyyy): ')

if len(re.findall(regExp4, date_input)) > 0:
    print(re.sub(regExp5, '-', date_input))
else:
    print('Введен некорректный формат')
