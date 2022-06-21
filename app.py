from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
# Setup the secret key and the environment
app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23',
                  ENV='development')


def get_users():
    users = {'user_1': {'name': 'moshe', 'email': 'moshe@gmail.com'},
             'user_2': {'name': 'yossi', 'email': 'yossi@gmail.com'},
             'user_3': {'name': 'simon', 'email': 'simon@gmail.com'},
             'user_4': {'name': 'haim', 'email': 'haim@gmail.com'},
             'user_5': {'name': 'itzik', 'email': 'itzik@gmail.com'}}
    return users


def search_user(input):
    users = get_users()

    try:
        user = users[input]
        return 'This User info is: Name: ' + user['name'] + ', Mail: ' + user['email']
    except:
        if len(input) == 0:
            return 'The users are: user_1, user_2, user_3, user_4, user_5'

        return 'This username does not exist (existing users are: user_1...user_5)'


def register_user(username, nickname):
    users = get_users()
    if username in users:
        user = users[username]
        return "Hello: " + user['name']
    else:
        return "Hello: " + nickname


@app.route('/')  # render homepage
def homepage():
    return render_template('homepage.html')


@app.route('/contact/')  # render contact page
def contact():
    return render_template('contact.html')


@app.route('/assignment3_1/')  # render ‘assignment3_1 page
def assignment3_1():
    return render_template('assignment3_1.html',
                           albums=['Rust in Peace', '...And Justice for all', 'PowerSlave', 'Innfestissuman',
                                   'Ascendancy'])


@app.route('/assignment3_2/')  # render ‘assignment3_2 page
def assignment3_2():
    return render_template('assignment3_2.html')


@app.route('/search', methods=['GET'])
def my_search_form():
    text = request.args.get('text')
    processed_text = search_user(text)
    return render_template('assignment3_2.html', processed_text=processed_text)


@app.route('/register', methods=['POST'])
def my_register_form():
    register_username = request.form['register_username']
    register_nickname = request.form['register_nickname']
    register_text = register_user(register_username, register_nickname)
    session['register_text'] = register_text
    return render_template('assignment3_2.html', register_text=session.get(session['register_text']))


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('assignment3_2'))


@app.route('/github/')
def github():
    return redirect('https://github.com/lironbdolah')


@app.route('/refirect_for/')
def refirect_for():
    return redirect(url_for('assignment3_1'))


if __name__ == '__main__':
    app.run(debug=True)
