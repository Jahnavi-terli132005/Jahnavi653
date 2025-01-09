from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure this file is inside a 'templates' folder

@app.route('/shuffle')
def shuffle():
    # Create a random configuration of the 8-puzzle (3x3 grid)
    numbers = list(range(1, 9)) + [None]  # The 'None' represents the empty tile
    random.shuffle(numbers)
    board = [numbers[i:i+3] for i in range(0, 9, 3)]  # Create a 3x3 matrix from shuffled numbers
    return jsonify({'board': board})  # Return the board as JSON

if __name__ == '__main__':
    app.run(debug=True)