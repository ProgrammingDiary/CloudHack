from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Merchant

app = Flask(__name__)

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def Home():

@app.route('/userLogin', methods=['GET', 'POST'])
def userLogin():
	if request.method == 'POST':

	else:
		return render_template()
