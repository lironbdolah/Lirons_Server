import json

from flask import render_template, session, Blueprint, jsonify, make_response, Response
from utilities.functions import *

assignment4_users = Blueprint('assignment4_users', __name__, static_folder='static',
                              static_url_path='/assignment4_users', template_folder='templates')


@assignment4_users.route('/assignment4/users', methods=['GET', 'POST'])
def display_json():
    table = get_table()
    json_data = []
    row_headers = [x[0] for x in mycursor.description]
    for result in table:
        json_data.append(json.dumps(dict(zip(row_headers, result))))
    return render_template('assignment4_users.html', data={
        'jsondata': json_data})
