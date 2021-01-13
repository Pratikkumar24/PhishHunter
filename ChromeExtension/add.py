from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def check():
    