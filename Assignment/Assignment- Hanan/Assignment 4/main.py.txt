Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask,render_template,request,redirect,url_for
... app=Flask(__name__)
... 
... @app.route("/")
... def home_page():
...     return render_template("register.html")
... 
... if(__name__=='__main__'):