import flask
from flask import request
from Controllers import UserController, PasswordController

app = flask.Flask(__name__)

"""
User Functions
"""
@app.route('/api/v1.0/User/login', methods=['POST'])
def user_login():
    json_data = request.get_json()
    return UserController.login(json_data['username'], json_data['password'])
@app.route('/api/v1.0/User/signup', methods=['POST'])
def user_signup():
    json_data = request.get_json()
    return UserController.signup(json_data['username'], json_data['password'], json_data['email'], json_data['firstname'], json_data['lastname'])

"""
Password Functions
"""
@app.route('/api/v1.0/Password/insert', methods=['POST'])
def password_insert():
    json_data = request.get_json()
    return PasswordController.insert(json_data['password_type'], json_data['password_name'], json_data['password_user'], json_data['password_site'], json_data['password_password'], json_data['password_note'], json_data['password_user_id'])
@app.route('/api/v1.0/Password/delete', methods=['POST'])
def password_delete():
    json_data = request.get_json()
    return PasswordController.delete(json_data['password_id'])
@app.route('/api/v1.0/Password/generate', methods=['POST'])
def password_generate():
    json_data = request.get_json()
    return PasswordController.generate_password(json_data['password_length'], json_data['include_special_characters'], json_data['verify_not_pwned'])
@app.route('/api/v1.0/Password/password_pwned_count', methods=['POST'])
def password_pwned_count():
    json_data = request.get_json()
    return PasswordController.password_pwned_count(json_data['password'])
@app.route('/api/v1.0/Password/get_all_user_passwords', methods=['POST'])
def get_all_user_passwords():
    json_data = request.get_json()
    return PasswordController.get_all_user_passwords(json_data['user_id'], json_data['user_password'])

"""
Launch API
"""
if __name__ == '__main__':
    app.run(host="localhost", port=8092, debug=False, ssl_context='adhoc')
