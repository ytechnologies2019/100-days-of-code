from os import makedev

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('Hello')


@app.route('/username/<name>/<int:number>')
def greet(name , number):
    return f'Hello , {name} , your age is {number} years old'

if __name__ == "__main__":
    app.run(debug=True)