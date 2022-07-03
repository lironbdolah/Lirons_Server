import mysql.connector

## connections
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_users"
    )
    mycursor = mydb.cursor()
except:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()

    # create db
    mycursor.execute("CREATE DATABASE db_users")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_users"
    )

    mycursor = mydb.cursor()

    # create table
    mycursor.execute("CREATE TABLE users (id int PRIMARY KEY , email VARCHAR(20)  ,  user_name CHAR(20))")

    from random import randint, randrange

    x = randint(100, 9999999)

    # insert users to the table
    val = [(randint(999999, 9999999), 'moshe@gmail.com', 'moshe'),
           (randint(999999, 9999999), 'yossi@gmail.com', 'yossi'),
           (randint(999999, 9999999), 'simon@gmail.com', 'simon'),
           (randint(999999, 9999999), 'haim@gmail.com', 'haim'),
           (randint(999999, 9999999), 'itzik@gmail.com', 'itzik')]

    # insert row
    sql = "INSERT INTO users (id,email, user_name) VALUES (%s ,%s, %s )"
    for v in val:
        mycursor.execute(sql, v)
    mydb.commit()


def get_table():
    mycursor.execute("SELECT * FROM users")
    table = mycursor.fetchall()
    return table


def get_email():
    mycursor.execute("SELECT email FROM users")
    m = mycursor.fetchall()
    emails = [i for sub in m for i in sub]
    return emails


def get_ids():
    mycursor.execute("SELECT id FROM users")
    m = mycursor.fetchall()
    ids = [i for sub in m for i in sub]
    return ids


def get_user():
    mycursor.execute("SELECT user_name FROM users")
    u = mycursor.fetchall()
    users = [i for sub in u for i in sub]
    return users
