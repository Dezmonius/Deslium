# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('Clients.sqlite')
c = conn.cursor()

def add_client(idPatient,idDoctor,patient,timeofaccept):
    c.execute("INSERT INTO patients (idPatient,idDoctor,patient,timeofaccept) VALUES('%s','%s','%s','%s')"%(idPatient,idDoctor,patient,timeofaccept))
    conn.commit()

idPatient = input("Введи id пациента\n")
idDoctor = input("Введи id доктора\n")
patient = input("Введи имя пациента\n")
timeofaccept = input("Введи время приема\n")
print('\n')

add_client(idPatient,idDoctor,patient,timeofaccept)
c.execute('SELECT * FROM patients')
row = c.fetchone()

c.close()
conn.close()

