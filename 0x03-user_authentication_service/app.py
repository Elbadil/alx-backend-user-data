#!/usr/bin/env python
"""Defining a Flask App"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def bienvenue():
    """returns Bienvenue as Json message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Registers a user in the db if not already exists"""
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    try:
        user = AUTH.register_user(user_email, user_pwd)
        return jsonify(
            {'email': f'{user.email}',
             'message': 'user created'})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Create a session id for a user and sets cookie to session_id"""
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    valid_info = AUTH.valid_login(user_email, user_pwd)
    if valid_info is False:
        abort(401)  # Unauthorized

    session_id = AUTH.create_session(user_email)
    json_response = jsonify({"email": f"{user_email}",
                             "message": "logged in"})
    json_response.set_cookie('session_id', session_id)
    return json_response

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """"""
    session_id = request.cookie.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect('bienvenue')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
