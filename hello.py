from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    first_name = "King"
    television = ['Hisense', 'Sharp', 'Samsung', 'LG']
    return render_template("index.html", 
        first_name=first_name,
        television=television) 



@app.route("/user/<name>")
def user(name):
     return render_template("user.html", user_name=name) 



# Invalid Error
@app.errorhandler(404)
def page_not_find(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_find(e):
    return render_template("500.html"), 500