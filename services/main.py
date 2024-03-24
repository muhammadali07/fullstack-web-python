from flask import Flask, render_template, request, flash, redirect, url_for

# import fucntion from app
import app as service

app = Flask(__name__)
app.debug = True # auto reload when change the file

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(username, password)
    res , err = service.login(username, password)
    if err != None:
        print(err)
        return redirect(url_for(index))
    elif len(res) > 0:
        return redirect(url_for(dashboard))
    else:
        return redirect(url_for(index))
 
    
# redirect page
def dashboard():
    return render_template('dashboard.html')
    