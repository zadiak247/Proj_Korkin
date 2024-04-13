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

"""
with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("INSERT INTO TV_repair VALUES ('Samsung', 'Ростсельмаш', 12776.99, '11/12/2024', 'A32', 'Виктор', 5000.99)")
"""

with sq.connect('tm.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM TV_repair")
    result = cur.fetchall()
    print(f'Содержание таблицы "Ремонт телевизоров": {result}')
