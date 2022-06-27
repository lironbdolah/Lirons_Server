from flask import Flask
from utilities.functions import *
import mysql.connector
###### App setup
app = Flask(__name__)

app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23',
                  ENV='development')

###### Pages
## assignment4
from pages.assignment4.assignment4 import assignment4
app.register_blueprint(assignment4)

from pages.assignment4_users.assignment4_users import assignment4_users
app.register_blueprint(assignment4_users)

from pages.assignment4_outer_source.assignment4_outer_source import assignment4_outer_source
app.register_blueprint(assignment4_outer_source)


from pages.assignment4_restapi.assignment4_restapi import assignment4_restapi
app.register_blueprint(assignment4_restapi)

if __name__ == '__main__':
    app.run(debug=True)


