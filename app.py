from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_random', methods=['POST'])
def generate_random():
    data = request.json
    start = int(data.get('start', 1))
    end = int(data.get('end', 100))
    
    # Generate a random integer between start and end (inclusive)
    random_number = random.randint(start, end)
    
    return jsonify({'number': random_number})

if __name__ == '__main__':
    app.run(debug=True)