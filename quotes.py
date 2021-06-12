from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DATABASE_URI'] = 'postgres://zoiptishlvcovd:3322b2cf059f2b64ef9598d4280b9b2a6a24d47238a7071e016ae3911a51da32@ec2-54-163-97-228.compute-1.amazonaws.com:5432/d6rqtgojd196tg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))
@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')
@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
