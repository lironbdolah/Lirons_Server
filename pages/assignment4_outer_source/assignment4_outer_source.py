import requests
from flask import render_template,Blueprint,request,session,jsonify,make_response
from utilities.functions import *
import json


assignment4_outer_source = Blueprint('assignment4_outer_source', __name__,
                                     static_folder='static', static_url_path='/assignment4_outer_source',
                                     template_folder='templates')

@assignment4_outer_source.route('/assignment4/outer_source')
def index():
    session.clear()
    return render_template('assignment4_outer_source.html')

@assignment4_outer_source.route('/assignment4/outer_source', methods=['POST'])
def display_outer_json():
    session.clear()
    id = request.form['singleuser_id']
    uri = "https://reqres.in/api/users/%s"% (str(id),)
    print(uri)
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    print(data)
    session['user_data'] = json.dumps(data)
    return render_template('assignment4_outer_source.html',register_text=session.get(session['user_data']))
