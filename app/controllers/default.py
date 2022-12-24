from flask import render_template
from app import app, db

from app.models.forms import LoginForm
from app.models.tables import User

@app.route("/index/<j>") 
@app.route("/index",defaults={'j':None})
def index(j):
    return render_template('index.html',j=j)


@app.route("/login", methods=["GET", "POST"])
def login():
   form = LoginForm()
   return render_template('login2.html',
                           form=form)

@app.route("/teste/<info>") 
@app.route("/teste", defaults={'info': None})
def teste(info):
   i = User("LucasVictor", "123","Lucas Victor","lucasvictor1910@gmail.com")
   db.session.add(i)
   db.session.commit()
   


   # if info:
   #    return f"Olá, {info} !"   
   # else:
   #    return "Olá, usuário !"
