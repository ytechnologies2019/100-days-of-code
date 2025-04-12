from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    random_number = random.randint(1, 10)
    today         = datetime.today()
    this_year     = today.year
    return render_template('index.html' , number=random_number , copyright_year=this_year)