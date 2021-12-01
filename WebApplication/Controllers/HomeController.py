from WebApplication import app
from flask import request
import string

@app.route('/<nick_name>', methods=['GET'])
def index(nick_name: string):
    body_data = request.get_json(force=True)
    print(f"My name is {body_data['first_name']} {body_data['last_name']} ({nick_name})")
    return f"My name is {body_data['first_name']} {body_data['last_name']} ({nick_name})"