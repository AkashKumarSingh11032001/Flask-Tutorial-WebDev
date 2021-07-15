from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # ---> Importing html file to flask
    return render_template("index.html")

@app.route("/about")
def about():
    # ---> Importing html file to flask
    return render_template("about.html")

app.run(debug=True)