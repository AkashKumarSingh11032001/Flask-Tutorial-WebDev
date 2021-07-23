from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    # ---> Importing html file to flask
    return render_template("index.html")

@app.route("/about")
def about():
    # ---> Importing html file to flask
    return render_template("about.html")

@app.route("/contact")
def contact():
    # ---> Importing html file to flask
    return render_template("contact.html")

@app.route("/post")
def post():
    # ---> Importing html file to flask
    return render_template("post.html")

app.run(debug=True)