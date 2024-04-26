import email
from os import name

import psycopg2

host = 'localhost'
user = 'postgres'
password = 'Asadbek_752'
database = 'n42'
port = 5432

conn = psycopg2.connect(database=database,
                        user=user,
                        password=password,
                        host=host,
                        port=port)
cur = conn.cursor()

cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
conn.commit()


def read_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update_user(id, name):
    cur.execute("UPDATE users SET name = %s WHERE id = %s", (name, id))
    conn.commit()


def delete_user(id):
    cur.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()


def create_user(param, param1):
    pass


create_user("John Doe", "john.doe@example.com")
read_users()
update_user(1, "Jane Doe")
delete_user(1)

# Kursor va bog'lanishni yopish
cur.close()
conn.close()
