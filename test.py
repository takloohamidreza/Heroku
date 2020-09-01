import sqlite3

connection =  sqlite3.connect('data.db')
cursor = connection.cursor()

Creat_Table = 'CREATE TABLE users (username text, password text,id int)'
cursor.execute(Creat_Table)

Users =[
    ('hamid','asdf',3)
    ,('reza','fasd',2)
    ,('hamidreza','asdffasd',1)
]

Insert = 'INSERT INTO users VALUES (?,?,?)'
cursor.executemany(Insert,Users)

Select = 'SELECT * FROM users '

for x in cursor.execute(Select):
    print(x)

connection.commit()


connection.close()
