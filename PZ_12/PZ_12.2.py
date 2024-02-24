"""
Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия'] получить новый список, в котором
длина слов не превышает 5 символов.
"""

spis = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']

# s_spis = []
# for i in range(len(spis)):
#     if len(spis[i]) <= 5:
#         s_spis.append(spis[i])

s_spis = [i for i in spis if len(i) <= 5]

print(f'Исходный список: {spis}\n', f'Список, длина слов которого не превышает 5 символов: {s_spis}')
