from Service.IUserService import IUserService
from Service.UserService import UserService
from WebApplication import app
from flask import request

from WebApplication.Models.User import User

@app.route('/SignUp', methods=['POST'])
def SignUp():
    # Data extraction
    body_data = request.get_json(force=True)
    user: User = User()
    user.UserName = body_data['UserName']
    user.FirstName = body_data['FirstName']
    user.LastName = body_data['LastName']
    user.Password = body_data['Password']
    
    # Passing data to business layer
    user_service: IUserService = UserService()
    user_service.sign_up(user)

    # Return response
    return "Success"