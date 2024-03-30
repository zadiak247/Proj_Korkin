"""
В исходном текстовом файле (dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ. Посчитать количество дат в
каждом формате. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
"""

import re

# [0-90-9.0-90-9.0-90-90-90-9]
# [0-90-9/0-90-9/0-90-90-90-9]
# [\d{2}((.)|(/))\d{2}((.)|(/))\d{4}]

with open("dates.txt", "r") as z:
    z_e = z.read()
    first_e = re.findall(re.compile(r"\d{2}\.\d{2}\.\d{4}"), z_e)
    second_e = re.findall(re.compile(r"\d{2}/\d{2}/\d{4}"), z_e)
    third_e = re.findall(re.compile(r"\d{2}/02/\d{4}"), z_e.replace('.', '/'))

print(f'Даты в формате ДД.ММ.ГГГГ:{first_e} \nДаты в формате ДД/ММ/ГГГГ:{second_e}')
print(f'Количество дат в формате ДД.ММ.ГГГГ : {len(first_e)};\n Количество дат в формате ДД/ММ/ГГГГ : {len(second_e)};')

with open("dates_feb.txt", "w") as z:
    z.write(str(f'{[third_e[i] for i in range(len(third_e))]}').replace(',', '\n').replace('[', '').replace(']', '')
            .replace("'", '').replace(" ", ''))
