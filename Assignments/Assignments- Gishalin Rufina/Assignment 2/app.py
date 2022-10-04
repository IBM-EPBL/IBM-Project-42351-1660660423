from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('homePage.html')


@app.route("/aboutpage")
def AboutPage():
    return render_template('AboutPage.html')

@app.route("/signup")
def signup():
    return render_template('SignUp.html')


@app.route("/signIn")
def signIn():
    return render_template('Sign-in.html')

