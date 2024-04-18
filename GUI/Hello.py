from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('static.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

#To run this at 127.0.0.1:5000 
#flask --app GUI/Hello.py run
#To run in a better mode for reloads try this
#flask --app GUI/Hello.py run --debugger --reload