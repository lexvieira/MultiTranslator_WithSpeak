from flask import Flask, request
from app.pyTranslateMulti import translate
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)

CORS(app) # 	

@app.route('/')
def hello_world():
    return render_template("html/index.html")

@app.route('/translator')
def translator():
    # here we want to get the value of user (i.e. ?user=some-value)
    text = request.args.get('text')   
    translations = translate(text) 
    return translations

