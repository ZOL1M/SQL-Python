import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

users_list = []
for user in users:
    user_dict = {
        'id': user[0],
        'name': user[1]
    }
    users_list.append(user_dict)

for user in users_list:
    print(user)

connection.commit()
connection.close()