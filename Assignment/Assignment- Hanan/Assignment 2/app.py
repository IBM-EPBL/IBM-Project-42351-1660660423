from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('HomePage.html')


@app.route("/aboutpage")
def AboutPage():
    return render_template('About.html')

@app.route("/signup")
def signup():
    return render_template('SignUp.html')


@app.route("/signIn")
def signIn():
    return render_template('SignI
n.html')
