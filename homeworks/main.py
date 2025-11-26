
# Создание и отпавка email с помощью html-шаблона, + вставка переменных в текст, + вложения


# from email.message import EmailMessage
# import smtplib
# from string import Template
# from pathlib import Path

# my_email = EmailMessage()

# cwd = Path("D:/") / "learning" / "homeworks" / "templates"
# # cwd = Path("homeworks") / "templates"
# imd = Path("D:/") / "learning" / "homeworks" / "images"

# html_template = Template((cwd/"index.html").read_text())
# html_content = html_template.substitute({'name': 'Pavel', 'date': 'tommorow'})

# my_email['from'] = 'Pavel <novikevichp@gmail.com>'
# my_email['to'] = 'friend@gmail.com'
# my_email['subject'] = "Let's go out"
# my_email.set_content(html_content, 'html')

# with open(imd / "webp.webp", "rb") as w_img:
#     image_data = w_img.read()
#     my_email.add_attachment(image_data, maintype='image', subtype="webp", filename="webp.webp")


# with open(imd / "pentium.jpg", "rb") as p_img:
#     image_data = p_img.read()
#     my_email.add_attachment(image_data, maintype='image', subtype="jpg", filename="pentium.jpg")


# with smtplib.SMTP(host='localhost', port='2525') as smtp_server:
#     smtp_server.ehlo()
#     smtp_server.send_message(my_email)
#     print('The message was sent')








# Создание, запись, чтение в БД


# import sqlite3

# DB_NAME = "sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sql_connection:
#     print(sql_connection)

    
# with sqlite3.connect(DB_NAME) as sqlite_cr:
#     sql_req = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#         );"""
#     sqlite_cr.execute(sql_req)


# added_dates = [
#     (1, "QA Course Stormnet", 17, 4),
#     (2, "QA Course Ksendzov", 1500, 53),
#     (3, "Python course", 50, 27)
# ]

# with sqlite3.connect(DB_NAME) as add_touple_in:
#     sql_req = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     #add_touple_in.execute(sql_req, added_dates)
#     for course in added_dates:
#         add_touple_in.execute(sql_req, course)
#     add_touple_in.commit()



# with sqlite3.connect(DB_NAME) as read_table:
#     sql_req = "SELECT * FROM courses"
#     sql_cursor = read_table.execute(sql_req)
#     for text in sql_cursor:
#         print(text)
#     records = sql_cursor.fetchall()
#     print(records)
#     # Вернет весь спиоск кортежей, при это цикл FOR не должен быть запущен
















# import array

# my_int_array = array.array("i", [4, 5, 10, 5, 7, 5])

# print(my_int_array.count(5))
# # Вывод кол-ва раз повторений элементов в массиве
# my_int_array.pop()
# print(my_int_array)
# # Delete last character
# print(len(my_int_array))

# with open("my_array.bin", "wb") as my_file:
#     my_int_array.tofile(my_file)
#     print("Success")
 
# imported_array = array.array("i")

# with open("my_array.bin", "rb") as import_file:
#     imported_array.fromfile(import_file, 3)
#     print(f"File was imported successfully. Your array is {imported_array}")



# my_dict = {}

# for i in range(1, 4):
#     key = input("Enter  key: ").strip()
#     value = input("Enter value: ").strip()
#     my_dict[key] = value  

# print(my_dict)



int = 10467

print(int % 1000 // 100)










# import sys

# print(sys.argv)

