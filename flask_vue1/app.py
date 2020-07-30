from flask import Flask, render_template, request, session, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax/<id>', methods=['GET'])
def ajax(id):
    data = {
        1:{'id':1, 'name':'Taro', 'mail':'taro@yamada'},
        2:{'id':2, 'name':'Hanako', 'mail':'hanako@flower'},
        3:{'id':3, 'name':'Sachiko', 'mail':'sachico@happy'}
    }
    n = int(id)
    if n < 1:
        n = 1
    if n > len(data):
        n = 3
    return jsonify(data[n]);
	
if __name__=='__main__':
	app.debug = True
	app .run()