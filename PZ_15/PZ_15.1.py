"""
Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по ремонту бытовой техники. БД должна содержать таблицу
Ремонт телевизоров, имеющую следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена, Дата ремонта,
Документ, Мастер, Сумма оплаты.
"""

import sqlite3 as sq

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS TV_repair")
    cur.execute("""CREATE TABLE IF NOT EXISTS TV_repair (
    TV_brand TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    price FLOAT NOT NULL,
    repair_date DATE NOT NULL,
    doc VARCHAR NOT NULL,
    master TEXT NOT NULL,
    payment FLOAT NOT NULL
    )""")

info_tm = [
    ('Samsung', 'Ростсельмаш', 11776.99, '11/12/2024', 'A32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 12776.99, '12/12/2024', 'Б32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 13776.99, '13/12/2024', 'В32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 14776.99, '14/12/2024', 'Г32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 15776.99, '15/12/2024', 'Д32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 16776.99, '16/12/2024', 'Е32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 17776.99, '17/12/2024', 'Ё32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 18776.99, '18/12/2024', 'Ж32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 19776.99, '19/12/2024', 'З32', 'Виктор', 50000.99),
    ('Samsung', 'Ростсельмаш', 20776.99, '20/12/2024', 'И32', 'Витя', 50000.99)
]

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO TV_repair VALUES (?, ?, ?, ?, ?, ?, ?)", info_tm)


with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM TV_repair")
    result = cur.fetchall()
    print(f'Полное содержание таблицы "Ремонт телевизоров":\n{result}')

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM TV_repair WHERE price<15000")
    result = cur.fetchall()
    print(f'Содержание таблицы "Ремонт телевизоров", где цена нменьше 15000:\n{result}')

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM TV_repair WHERE price>15000")
    result = cur.fetchall()
    print(f'Содержание таблицы "Ремонт телевизоров, где цена больше 15000":\n{result}')

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE TV_repair SET price = price+4 WHERE master='Виктор'")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE TV_repair SET price = price+4000 WHERE master!='Виктор'")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE TV_repair SET price = price+20000 WHERE price>20000")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM TV_repair WHERE doc='И32'")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM TV_repair WHERE master!='Виктор'")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM TV_repair WHERE price>20000")

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM TV_repair")
    result = cur.fetchall()
    print(f'Итоговое содержание таблицы "Ремонт телевизоров":\n{result}')
