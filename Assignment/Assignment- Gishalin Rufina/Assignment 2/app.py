from flask import Flask, url_for, render_template

import sqlite3 as sql


app = Flask(__name__)
app.secret_key="123"




@app.route("/")
def homePage():
    return render_template('homePage.html')


@app.route("/aboutpage")
def AboutPage():
    return render_template('AboutPage.html')

@app.route("/signup")
def signup():
    return render_template('SignUp.html')

@app.route('/register', methods = ['POST','GET'] )
def register():
    if request.method == 'POST':
        try:
            FirstName = request.form['firstname']
            MiddleName = request.form['middlename']
            LastName = request.form ['lastname']
            PhoneNumber = request.form ['phone']
            Address=request.form ['address']
            Email=request.form ['email']
            Password=request.form ['pass']

            with sql.connect("database.db") as con:
              cur = con.cursor()
              cur.execute("INSERT INTO User_Details ( FirstName,MiddleName, LastName,PhoneNumber, Address, Email, Password ) VALUES (?,?,?,?)",(FirstName,MiddleName, LastName,PhoneNumber, Address, Email, Password) )
              con.commit()
              msg = "Record successfully added!"
        except:
         con.rollback()
         msg = "error in insert operation"


        finally:
          return render_template("list.html",msg = msg)
          con.close()
      
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   
   cur = con.cursor()
   cur.execute("select * from User_Details")
   
   User_Details = cur.fetchall();
   return render_template("list.html" )

@app.route("/signIn")

def signIn():
    return render_template('Sign-in.html')



