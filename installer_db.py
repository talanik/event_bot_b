import sqlite3

from Class.db import DB


conn = sqlite3.connect("maindb.db")
cursor = conn.cursor()

# cursor.execute("DROP TABLE orders")
cursor.execute("""CREATE TABLE if not exists localize (
                                                        alias text, 
                                                        ru text, 
                                                        uz text
                                                     )""")

cursor.execute("""CREATE TABLE if not exists users (
                                                        user_id int, 
                                                        user_name text, 
                                                        phone text,
                                                        edu text,
                                                        chat_id int,
                                                        lang text
                                                     )""")

cursor.execute("""CREATE TABLE if not exists temp_users (
                                                        user_id int, 
                                                        user_name text, 
                                                        phone text,
                                                        edu text,
                                                        chat_id int,
                                                        lang text
                                                     )""")

cursor.execute("""CREATE TABLE if not exists events (
                                                        event_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                                                        event_name text, 
                                                        event_name_uz text, 
                                                        event_desc text, 
                                                        event_desc_uz text, 
                                                        image text, 
                                                        event_date int,
                                                        event_limit int,
                                                        sended int default 0
                                                    )""")

cursor.execute("""CREATE TABLE if not exists orders (
                                                        user_id int, 
                                                        event_id int
                                                    )""")

cursor.execute("""CREATE TABLE if not exists agents (
                                                        agent_id int, 
                                                        department text, 
                                                        fio text
                                                    )""")

# cursor.execute("""UPDATE events SET sended=0 WHERE event_id=1""")
conn.commit()


# dd = cursor.execute("""SELECT * FROM events WHERE (event_date>1646140381 AND sended = 1 AND event_name LIKE 'Квиз-мафия%')""")
# res = dd.fetchone()
#
# print(res)
conn.close()

db = DB()
# db.insert(table='agents', columns=['agent_id','department','fio'],values=[523042204,'admin','Тимур'],closed=False)
# db.update(table='events', sets={'event_limit': 100}, conditions={'event_id': 1}, closed=False)
print(db.fetchall('localize', conditions={'alias':'back'}))