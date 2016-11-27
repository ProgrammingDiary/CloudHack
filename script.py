from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_weasyprint import HTML, render_pdf
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Merchant, Base, Bill
import pdfkit

app = Flask(__name__)

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

ucount = 1001
mcount = 5001

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/loginuser', methods=['GET', 'POST'])
def loginUser():
	if request.method == 'POST':
		userQuery = session.query(User).filter_by(email=request.form['email'])
		if userQuery.count() == 0:
			flash("Invalid Account")
			return redirect('/loginuser')
		else:
			currUser = userQuery.one()	
			if currUser.password == request.form['password']:
				flash("Registration Successfull")
				return redirect(url_for('Menu', userid=currUser.id), code=200)
			else:
				flash("Invalid Credentials")
				return redirect('/loginuser')
	else:
		return render_template('loginUser.html')

@app.route('/loginmerchant', methods=['GET', 'POST'])
def loginMerchant():	
	if request.method == 'POST':
		userQuery = session.query(Merchant).filter_by(email=request.form['email'])
		if userQuery.count() == 0:
			flash("Invalid Account")
			return redirect('/loginmerchant')
		else:
			currUser = userQuery.one()	
			if currUser.password == request.form['password']:
				flash("Registration Successfull")
				return redirect('/')
			else:
				flash("Invalid Credentials")
				return redirect('/loginmerchant')
	else:
		return render_template('loginMerchant.html')

@app.route('/registermerchant', methods=['GET', 'POST'])
def registerMerchant():
	global mcount
	if request.method == 'POST':
		mid = request.form['fullname'][0:2].upper() + str(mcount)
		mcount += 1
		newUser = Merchant(mid=mid, name=request.form['fullname'], email=request.form['email'],address=request.form['address'], password=request.form['password'])
		session.add(newUser)
		session.commit()
		if session.query(Merchant).filter_by(email=request.form['email']).count() != 0:
			flash("Merchant already registered.")
			return redirect(url_for('registerMerchant'))
		else:
			flash("Registration Successfull")
			return redirect('/')
	else:
		return render_template('registerMerchant.html')

@app.route('/registeruser', methods=['GET', 'POST'])
def registerUser():
	global ucount
	if request.method == 'POST':
		uid = request.form['fullname'][0:2] + str(ucount)
		ucount += 1
		newUser = User(uid=uid, name=request.form['fullname'], email=request.form['email'], address=request.form['address'],password=request.form['password'])
		session.add(newUser)
		session.commit()
		if session.query(User).filter_by(email=request.form['email']).count() != 0:
			flash("User already registered.")
			return redirect(url_for('registerUser'))
		else:
			flash("Registration Successfull")
			return redirect('/')
	else:
		return render_template('registerUser.html')

<<<<<<< HEAD
@app.route('/detailsuser')
def detailsUser():
	Bills = session.query(Bill).all()	
	return render_template('detailsUser.html', Bill=Bills)
=======
@app.route('/generatebill', methods=['GET', 'POST'])
def generateBill():
	if request.method == 'POST':
		currUser = session.query(User).filter_by(email=request.form['email']).one()
		mid = 
		newBill = Bill(user_id=currUser.uid, ,description=request.form['description'], user_email=request.form['email'], warranty=request.form['warranty'], amount=request.form['amount'], )
>>>>>>> 0f2bb04ab04c04a762825d44211fe8924afd3c8b

if __name__ == '__main__':
	app.debug = True
	app.secret_key = 'some_secret'
	app.run(host='0.0.0.0', port=5000)