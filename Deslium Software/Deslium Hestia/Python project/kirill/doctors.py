# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('Clients.sqlite')
c = conn.cursor()

def add_doctor(id,name,speciality,info,dateofaccept,timeofaccept,patients):
    c.execute("INSERT INTO doctors (id,name,speciality,info,dateofaccept,timeofaccept,patients) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(id,name,speciality,info,dateofaccept,timeofaccept,patients))
    conn.commit()

id = input("Введи id доктора\n")
name = input("Введи имя доктора\n")
speciality = input("Введи специальность доктора\n")
info = input("Введи Информацию о докторе\n")
dateofaccept = input("Введи дату приема\n")
timeofaccept = input("Введи время приема\n")
patients = input("Введи пациентов\n")
print('\n')


add_doctor(id,name,speciality,info,dateofaccept,timeofaccept,patients)
c.execute('SELECT * FROM doctors')
row = c.fetchone()

c.close()
conn.close()
input("жмякни ентер")