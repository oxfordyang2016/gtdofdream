
from flask import Flask, render_template
app = Flask(__name__)




testdict = {'yangming':['try to add item','try to deal with home work'],'ma':['delete meanless task','try to clean house']}

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5],testdict = testdict)


@app.route("/youdu")
def template_test1():
    return render_template("youdu.html")

@app.route("/front")
def front():
    return render_template("front.html")

@app.route("/task")
def task():
    return render_template("task.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


       
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/receive")
def data():
    print("are u ok") 

if __name__ == '__main__':
    app.run(debug=True)








