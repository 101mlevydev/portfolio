import random
from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def generate_random():
    response = random.choice(['hot', 'cold'])
    return response

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
