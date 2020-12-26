from flask import Flask, request, jsonify,render_template,redirect,url_for
from model import db_connection
from controllers import authentication,contacts
from flask_cors import CORS, cross_origin
from functools import wraps
from time import time
import datetime
import jwt
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# auth=authentication.authenticate()
contacts = contacts.Contacts()

def validate_token(function):
    @wraps(function)
    def wrapper():
        data = request.get_json(force=True)

        input_data, status = authentication.authenticate(data)
        if status == "success":
            return function(input_data,time())  
        return status
    return wrapper

def main():
    app.run(debug=True)

@app.route('/')
@validate_token
def home(input,start_time):
    return jsonify({'time':time()-start_time})

@app.route('/login',methods=['POST'])
def login():
    data=request.get_json(force=True)
    user=data['user']
    expiration_time= datetime.datetime.utcnow() + datetime.timedelta(days=2)
    payload = {"user": user,"exp":expiration_time}
    token = jwt.encode(payload,"secret").decode('utf-8')
    return jsonify({"success":"success","token":token,"user":user})

@app.route('/create_contact',methods=['POST'])
@validate_token
def create_contact(input,start_time):
    result = contacts.create_contact(input)
    return jsonify(result)

@app.route('/add_contacts',methods=['POST'])
@validate_token
def add_contacts(input,start_time):
    result = contacts.add_contacts(input)
    return jsonify(result)

@app.route('/list_contacts',methods=['GET'])
@validate_token
def list_contacts(input,start_time):
    output = contacts.list_contact(input)
    return jsonify(output)

@app.route('/remove_contacts',methods=['POST'])
@validate_token
def remove_contacts(input,start_time):
    output = contacts.remove_contact(input)
    return jsonify(output)

@app.route('/search_contacts',methods=['POST'])
@validate_token
def search_contacts(input,start_time):
    output = contacts.search_contact(input)
    return jsonify(output)

@app.route('/update_contact',methods=['POST'])
@validate_token
def update_contact(input,start_time):
    output = contacts.update_contact(input)
    return jsonify(output)

if __name__ == '__main__':
    main()
