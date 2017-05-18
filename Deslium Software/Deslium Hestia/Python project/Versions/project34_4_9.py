import sqlite3

docs = []


class Doctor:
    available_time = ['08:00 - 08:30', '08:30 - 09:00', '09:00 - 09:30', '09:30 - 10:00', '10:00 - 10:30',
                      '10:30 - 11:00',
                      '11:00 - 11:30', '11:30 - 12:00', '12:00 - 12:30', '12:30 - 13:00', '13:00 - 13:30',
                      '13:30 - 14:00',
                      '15:00 - 15:30', '15:30 - 16:00', '16:00 - 16:30', '16:30 - 17:00']

    def __init__(self):
        self.name = ""  # даём атрибут уникального имени
        self.patients = []  # список пациентов
        self.dates = {}  # ключ - дата, значение - доступное время

    # функция, вызываемая функцией print(obj)
    def __str__(self):
        self.patients.sort(key=lambda p: p.time_of_receipt)
        self.patients.sort(key=lambda p: p.date_of_receipt)
        ret = ''
        for pat in self.patients:
            ret += pat.name + " записан на " + pat.time_of_receipt + " к " + self.name + " на " + pat.date_of_receipt + '\n'
        return ret

    # функция со сортированным списком записей для экспорта в бд
    def forbd(self):
        self.patients.sort(key=lambda p: p.time_of_receipt)
        self.patients.sort(key=lambda p: p.date_of_receipt)
        adder = []
        for pat in self.patients:
            addin = (pat.name + " записан на " + pat.time_of_receipt + " к " + self.name + " на " + pat.date_of_receipt)
            adder.append(addin)
        return adder

class Patient:
    name = ""
    date_of_receipt = ""
    time_of_receipt = ""


def createSchedule():  # основное тело программы
    def time(day):  # функция выбора времени для 16 пациентов на 8-ми часовой рабочий день
        for item in day:
            print("Доступное время: " + item)
            option_selected = int(
                input("Введите 1, если вас устраивает выбранное время, 2 - если хотите поискать другое.\n"))
            if option_selected == 1:
                return item

    doc_number = 0
    if len(docs) > 0:
        print("Выберите доктора:")
        print("0. Новый доктор")
        for i in range(len(docs)):
            print(str(i + 1) + '. ' + docs[i].name)  # выводим список докторов на экран
        doc_number = int(input())
    doc = None
    if doc_number == 0:
        doc = Doctor()
        doc.name = input('Введите ФИО доктора: \n')
        docs.append(doc)
    else:
        doc = docs[doc_number - 1]
    date = ''
    while date not in doc.dates:
        date = input('Введите дату записи пациентов для приёма специалиста: \n')
        if date not in doc.dates:
            doc.dates[date] = list(Doctor.available_time)  # копируем список доступного времени на определённую дату

    for i in range(len(doc.dates[date])):  # создаём пациентов для доктора
        pat = Patient()  # создаём пациента
        pat.name = input('Введите ФИО пациента (оставьте строку пустой для выхода в меню): \n')
        if pat.name == "":
            break
        pat.date_of_receipt = date
        pat.time_of_receipt = time(doc.dates[date])  # генерируем для пациента время приёма при помощи вызова функции
        print(
            "Пациент " + pat.name + " успешно записан на " + pat.time_of_receipt + " к доктору " + doc.name + " на " + date)  # вывод результата
        doc.dates[date].remove(pat.time_of_receipt)
        doc.patients.append(pat)
    if len(doc.dates[date]) == 0:
        print("\nСвободного времени для записи на текущую дату к выбранному специалисту больше нет.")


def bd_add(id, note):
    conn = sqlite3.connect('schedule.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS sheet (id integer, note varchar)')
    c.execute("INSERT INTO sheet (id, note) VALUES ('%s','%s')"%(id, note))
    conn.commit()
    c.close()
    conn.close()


def bd_clear():
    conn = sqlite3.connect('schedule.sqlite')
    c = conn.cursor()
    c.execute("drop  table if exists sheet")
    conn.commit()
    c.close()
    conn.close()


def bd_read():
    con = sqlite3.connect('schedule.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM sheet')
    bdtoread = cur.fetchall()
    for j in bdtoread:
        print(j)

    con.close()


while True:
    print("""
        Программа создаёт расписание приёма врачами пациентов.
        Все инструкции вы получите по ходу выполнения программы.
    Введите 1 чтобы составить новое расписание.
    Введите 2 чтобы просмотреть существующее расписание.
    Введите 3 чтобы очистить созданное расписание.
    Введите 4 чтобы выйти.
    ***********************
    <Работа с базой данных>
    Введите 11 чтобы экспортировать расписание в базу данных.
    Введите 12 чтобы очистить базу данных.
    Введите 13 чтобы просмотреть записи в базе данных.
    Введите 14 чтобы удалить существующую базу данных.  

    <<<6>>> ABOUT US <<<6>>>
        """)
    try:

        item_selected = int(input())
        if item_selected == 1:
            createSchedule()
        elif item_selected == 2:
            for doc in docs:
                print(doc)
        elif item_selected == 3:
            docs.clear()
            print("Расписание успешно очищено!")
        elif item_selected == 4:
            break

        # добавление
        elif item_selected == 11:
            n = 1
            for doc in docs:
                records = doc.forbd()
                for i in range(len(records)):
                    bd_add(n, records[i])
                    n += 1
            print("Экспорт в базу данных 'schedule.sqlite' прошёл успешно.")
        # очистка
        elif item_selected == 12:
            bd_clear()
            print("База данных очищена от предыдущих записей.")
        # чтение из бд
        elif item_selected == 13:
            bd_read()
        # удаление бд
        elif item_selected == 14:
            print("Эта функция ещё не добавлена")

        elif item_selected == 6:
            print(''' 
            Проект по дисциплине "Программирование"
            Номер проекта: 34
            Описание задания:
                Расписание приема врача.
                Создайте класс Patient и класс Doctor.
                Пусть доктор может принять несколько пациентов, установите расписание того,
                    как доктор будет принимать 16 пациентов в течение 8 часового рабочего дня.

            Выполнили:
            Смирнов Николай Николаевич (Группа: ПИН-1)
            Кармицкий Кирилл Сергеевич (Группа: ПИН-1)
            ''')
        else:
            print("Такого пункта в меню нет.")
    except:
        continue
