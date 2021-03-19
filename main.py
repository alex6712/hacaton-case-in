from flask import Flask, request, render_template
from markupsafe import escape

import mysql.connector

app = Flask(__name__)
my_db = mysql.connector.connect(
  host="localhost",
  user="alex6712",
  password="123456789"
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/login')
def do_the_login():
    return 'not l'


@app.route('/login')
def show_the_login_form():
    return 'l'


if __name__ == "__main__":
    app.run()
