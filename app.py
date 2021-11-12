from flask import Flask, request
from pyTranslateMulti import translate
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Jardel, Cuzão, Servidor Python rodando!!! kkkkkk</h1>'

@app.route('/translator')
def translator():
    # here we want to get the value of user (i.e. ?user=some-value)
    text = request.args.get('text')   
    translations = translate(text) 
    return translations