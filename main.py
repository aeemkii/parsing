import mysql.connector
from db.group_sql import Group
from group_utils import group_action
from student_utils import student_action
import os


db = mysql.connector.connect(
host = "localhost",
user = "root",
password = "djh895kjh924y",
autocommit = True,
db = "students_db",
)

cursor = db.cursor()


print("Выберите действие: ")
print("""
    1. Редактирование групп
    2. Редактирование студента
""")

action_number = int(input("Введите номер действия: "))
if action_number == 1:
    group_action(cursor)
elif action_number == 2:
    student_action(cursor)


























# query = """SELECT booking.id, concat(user.first_name, ' ', user.last_name) as fullname,
#     status.name, booking.created, booking.check_in, booking.check_out
#     FROM booking LEFT JOIN user ON booking.user_id = user.id
#     LEFT JOIN status ON booking.status_id = status.id
#     ;"""
# cursor.execute(query)
# bookings = cursor.fetchall()
# for b in bookings:
#     print("--------------------------------------")
#     print(f"Номер брони: {b[0]}")
#     print(f"Ф.И.О.: {b[1]}")
#     print(f"Статус: {b[2]}")
#     print(f"Создано: {b[3]}")
#     print(f"Заселение: {b[4]}")
#     print(f"Выселение: {b[5]}")







