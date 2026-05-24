from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = '70f594022a8afdb5103839070bd91197f514a4f69efe2720'  # Replace with a secure secret key

# MongoDB connection setup
MONGO_URI = os.getenv('MONGO_URI')


client = MongoClient(MONGO_URI)
db = client['student_db']
collection = db['student_collection']

#API Routes
@app.route('/api')
def api():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# form submission route
@app.route('/submit', methods=['POST'])
def submit():

    name = request.form.get('name')
    email = request.form.get('email')
    course = request.form.get('course')

    try:
        student_data = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(student_data)

        flash("Data submitted successfully 🎉", "success")

    except Exception as e:
        flash("Failed to submit data ❌", "danger")

    return redirect(url_for('home'))

    try:
        collection.insert_one(student_data)
        return jsonify({'message': 'Data submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')

        todo_data = {
            "item_name": item_name,
            "item_description": item_description
        }

        mongo.db.todo_items.insert_one(todo_data)

        return jsonify({'message': 'To-Do item submitted successfully'}), 200
   


        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000, debug=True)
