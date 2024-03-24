from flask import Flask, render_template

app = Flask(__name__)
app.debug = True # auto reload when change the file

@app.route("/")
def hello_world():
    return render_template("home.html")