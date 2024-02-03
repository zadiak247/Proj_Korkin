"""
Средствами языка Python сформировать файл (.txt), содержащий последовательность из целых положительных и отрицательных
чисел. Сформировать новый текстовый файл  (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

Исходные данные:
Количество элементов:
Максимальный элемент:
Среднее арифметическое элементов первой трети:
"""

a = open('first.txt', 'w')
a.write(f'{input("Ввод последовательности целых чисел: ")}')
a.close()

a = open('first.txt', 'r')
nums = a.read()
a.close()

nums = nums.replace('.', '').replace(',', '').replace(';', '').split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

maxi = nums[0]
for i in range(len(nums)):
    if maxi <= nums[i]:
        maxi = nums[i]

z = 0

for i in range(len(nums)//3):
    z += nums[i]
z = z//(len(nums)//3)

b = open('second.txt', 'w')
b.write(f'Исходные данные: {nums}\n'
        f'Количество элементов: {len(nums)}\n'
        f'Максимальный элемент: {maxi}\n'
        f'Среднее арифметическое элементов первой трети: {z}\n')
b.close()

b = open('second.txt', 'r')
result = b.read()
b.close()

print(result)
