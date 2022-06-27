import requests
from flask import render_template,Blueprint,request,session,jsonify,make_response
from utilities.functions import *
import json


assignment4_restapi = Blueprint('assignment4_restapi', __name__,
                                     static_folder='static', static_url_path='/assignment4_restapi',
                                     template_folder='templates')

# @assignment4_restapi.route('/assignment4/restapi_users')
# def index():
#     session.clear()
#     return render_template('assignment4_restapi.html')

@assignment4_restapi.route('/assignment4/restapi_users/<int:custom_user>', methods=['GET'])
def project_page(custom_user):
    session.clear()
    ids = get_ids()
    print(ids)
    if custom_user in ids:
        table = get_table()
        json_data = []
        row_headers = [x[0] for x in mycursor.description]
        for result in table:
            if custom_user in result:
                json_data.append(dict(zip(row_headers, result)))
        session['custom_user'] = json.dumps(json_data)
        return render_template("assignment4_restapi.html", custom_user=custom_user,
                               register_text=session['custom_user'])
    else :
        custom_user = {'ERROR': 'No Existing user with stated ID'}
        session['custom_user'] = json.dumps(custom_user)
        return render_template("assignment4_restapi.html", custom_user=custom_user,
                               register_text=session['custom_user'])

@assignment4_restapi.route('/assignment4/restapi_users', methods=['POST', 'GET'])
def empty_page():
    session.clear()
    custom_user = 5796645
    table = get_table()
    json_data = []
    row_headers = [x[0] for x in mycursor.description]
    for result in table:
        if custom_user in result:
            json_data.append(dict(zip(row_headers, result)))
    session['custom_user'] = json.dumps(json_data)
    return render_template("assignment4_restapi.html", custom_user=custom_user, register_text=session['custom_user'])

@assignment4_restapi.route('/assignment4/restapi_users/', methods=['POST', 'GET'])
def empty_page_slash():
    session.clear()
    custom_user = 5796645
    table = get_table()
    json_data = []
    row_headers = [x[0] for x in mycursor.description]
    for result in table:
        if custom_user in result:
            json_data.append(dict(zip(row_headers, result)))
    session['custom_user'] = json.dumps(json_data)
    return render_template("assignment4_restapi.html", custom_user=custom_user, register_text=session['custom_user'])
