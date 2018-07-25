from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:118topcliff@localhost:5433/Height_Collector'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://zjecqprjtqcxbd:bac9791b06b4692913c94b67312c4a947ba5719de7cd62012778773a94ebe296@ec2-23-21-238-28.compute-1.amazonaws.com:5432/dctml8u0ded5cl?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data2"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.height_=height_
        self.email_=email_


@app.route("/")
def  index_1():
    return render_template("index.html")

@app.route("/success1111",methods=['POST'])
def success_1():
    if request.method=='POST':
        email=request.form["email_n"]
        height=request.form["height_n"]
        send_email(email,height)
        data=Data(email,height)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

if __name__=='__main__':
    app.debug=True
    app.run()
