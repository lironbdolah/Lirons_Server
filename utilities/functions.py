import mysql.connector

## connections
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bb201195",
  database="db_users"
)
mycursor = mydb.cursor()


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