from flask import Flask, jsonify
app = Flask(__name__)

users = []
next_id = 1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200
