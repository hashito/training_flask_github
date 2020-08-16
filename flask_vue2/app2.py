from flask import Flask, render_template, request, session, redirect, jsonify, g
import sqlite3

app = Flask(__name__)

# get Database Object.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('sample.sqlite3')
    return g.db


# close Dataabse Object.
def close_db(e=None):
    db = g.pop('db', None)


    if db is not None:
        db.close()
				
@app.route('/<id>', methods=['GET'])
def index(id):
    return render_template('index2.html', \
        title='Index', \
        message='※SQLite3 Database',
        id=id,
        alert='This is SQLite3 Database Sample!')


@app.route('/ajax/<id>', methods=['GET'])
def ajax(id):
    db = get_db()
    cur = db.execute("select * from mydata where id={id}".format(id=id))
    mydata = cur.fetchall()
    return jsonify(mydata);

if __name__=='__main__':
	app.debug = True
	app .run()