from flask import Flask, jsonify, request
app = Flask(__name__)

users = []
next_id = 1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return (jsonify(user), 200) if user else (jsonify({'error': 'Not found'}), 404)
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.json
    data['id'] = next_id
    next_id += 1
    users.append(data)
    return jsonify(data), 201
@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    user.update(data)
    return '', 204
