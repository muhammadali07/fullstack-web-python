from flask import Flask, render_template, request, flash, redirect, url_for

# import fucntion from app
import app

app = Flask(__name__)
app.debug = True # auto reload when change the file

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    print(request.form)
    username = request.form["username"]
    password = request.form["password"]
    res , e = app.login(username, password)
    if e != None:
        flash(e)
    elif len(res) > 0:
        return redirect(url_for(dashboard))
    else:
        print("gagal masihan")
 
    
# redirect page
def dashboard():
    return render_template('dashboard.html')
    