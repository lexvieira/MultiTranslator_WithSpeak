from flask import Flask, request
from pyTranslateMulti import translate
from flask_cors import CORS


app = Flask(__name__)

CORS(app) # 	

@app.route('/')
def hello_world():
    return '<h1>Jardel, Cuzão, Servidor Python rodando!!! kkkkkk</h1>'

@app.route('/translator')
def translator():
    # here we want to get the value of user (i.e. ?user=some-value)
    text = request.args.get('text')   
    translations = translate(text) 
    return translations

# app.run(host='0.0.0.0', port=os.environ.get('PORT', default=5000))
if __name__ == 'main':
	app.run(host='0.0.0.0')