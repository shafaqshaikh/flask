from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email





app =Flask(__name__)

ENV ='dev'
if ENV =='dev':
	app.debug= True
	app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:shafaq123@localhost/lexus'
else:
	app.debug= False
	app.config['SQLALCHEMY_DATABASE_URI']=''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db=SQLAlchemy(app)

class Feedback(db.Model):
	__tablename__='feedback'
	id = db.Column(db.Integer, primary_key=True)
	customer = db.Column(db.String(200))
	dealer = db.Column(db.String(200))
	rating = db.Column(db.Integer)
	comments = db.Column(db.Text())

	def __init__(self , customer , dealer , rating , comments):
		self.customer = customer
		self.dealer = dealer
		self.rating = rating
		self.comments = comments

db.create_all()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit' , methods=['POST'])
def submit():
	if request.method=='POST':
		customer =request.form['customer']
		dealer =request.form['dealer']
		rating =request.form['rating']
		comments =request.form['comments']
		#print(customer , dealer , rating , comments)
		if customer=='' or dealer=='':
			return(render_template('index.html' , message='please fill the required details'))

		if db.session.query(Feedback).filter(Feedback.customer==customer).count()==0:
			data = Feedback(customer , dealer , rating , comments)
			db.session.add(data)
			db.session.commit()
			return(render_template('success.html'))
			send_email(customer , dealer , rating , comments)


		return(render_template('index.html' , message='you have already submitted the feedback'))





if __name__ == '__main__':
	app.run()
