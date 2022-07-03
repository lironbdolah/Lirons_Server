from flask import render_template, request, session, Blueprint, jsonify, make_response
import mysql.connector
from random import randint
from utilities.functions import *

# catalog blueprint definition
assignment4 = Blueprint('assignment4', __name__, static_folder='static', static_url_path='/assignment4',
                        template_folder='templates')


def insert_user(username, email):
    emails = get_email()
    if email in emails:
        return 'this email is already taken'
    else:

        # get uniq id
        id = randint(100, 9999999)
        ids = get_ids()
        while id in ids:
            id = randint(100, 9999999)

        # insert user to the table
        val = (id, username, email)
        sql = "INSERT INTO users (id,user_name, email) VALUES (%s, %s, %s )"
        mycursor.execute(sql, val)
        mydb.commit()
        return 'the new user:' + username + " , " + email + ' has been entered'


# updates user name
def update_user(email, new_user):
    # check current user_name
    try:
        mycursor.execute("SELECT user_name FROM users WHERE email = %s", (email,))
        n = mycursor.fetchall()
        current_name = [i for sub in n for i in sub]

        if new_user != current_name[0]:
            ## update user name
            mycursor.executemany("UPDATE users SET user_name = %s WHERE email = %s ", [(new_user, email)])
            mydb.commit()
            return "user name updated! " + current_name[0] + " --> " + new_user
        else:
            return "This is already the user name"

    except:
        return "user does not exist in the database"


def delete_user(email):
    emails = get_email()
    if email in emails:
        ## delete user
        val = (email,)
        sql = "DELETE FROM users WHERE email = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        return 'The user with the email: ' + email + ' has been deleted from the Database'

    else:
        return 'Email is not in the Database'


# Routes
@assignment4.route('/')
def index_home():
    return render_template('assignment4.html')


@assignment4.route('/assignment4')
def index():
    return render_template('assignment4.html')


@assignment4.route('/assignment4/insertion', methods=['POST'])
def insertion_form():
    session.clear()
    insertion_username = request.form['insertion_username']
    insertion_email = request.form['insertion_email']
    insertion_text = insert_user(insertion_username, insertion_email)
    session['insertion_text'] = insertion_text
    return render_template('assignment4.html', register_text=session.get(session['insertion_text']))


@assignment4.route('/assignment4/update', methods=['POST'])
def update_form():
    session.clear()
    current_email = request.form['current_email']
    update_username = request.form['update_username']
    updates_text = update_user(current_email, update_username)
    session['updates'] = updates_text
    return render_template('assignment4.html', register_text=session.get(session['updates']))


@assignment4.route('/assignment4/delete', methods=['POST'])
def delete_form():
    session.clear()
    delete_email = request.form['delete_email']
    delete_text = delete_user(delete_email)
    session['delete'] = delete_text
    return render_template('assignment4.html', register_text=session.get(session['delete']))


@assignment4.route('/assignment4/display', methods=['GET', 'POST'])
def display_users():
    session.clear()
    users = get_user()
    session['users'] = str(users)
    return render_template('assignment4.html', register_text=session.get(session['users']))
