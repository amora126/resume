#import libraries and packages
from flask import Flask, render_template

#create our application
app = Flask(__name__)

#create our directory
@app.route('/')
def resume():
    return render_template("index.html")