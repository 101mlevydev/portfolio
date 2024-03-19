from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/feedback_db'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        candidate = request.form['candidate']
        questions = [request.form[f'question_{i}'] for i in range(1, 11)]
        feedback = {'candidate': candidate, 'answers': questions}
        mongo.db.feedback.insert_one(feedback)
        return redirect(url_for('dashboard'))
    return render_template('survey.html')

@app.route('/dashboard')
def dashboard():
    feedback_data = mongo.db.feedback.find()
    return render_template('dashboard.html', feedback_data=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)
