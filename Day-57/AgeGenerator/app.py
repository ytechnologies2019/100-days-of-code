from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/username/<name>')
def index(name):
    # Get gender
    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data.get('gender')

    # Get age
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data.get('age')

    return render_template('index.html', gender=gender, age=age, name=name)
