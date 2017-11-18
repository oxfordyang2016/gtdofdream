import os,time,json
from flask import Flask, request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
#in procfile to specify the python run the app
#web: FLASK_APP = server.py python -m flask run --host=0.0.0.0 --port=$PORT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name



class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    typeoftask = db.Column(db.String(80))
    task = db.Column(db.String(120), unique=True)

    def __init__(self, task):
        self.task = task
        self.date = str(time.time())

    def __repr__(self):
        return '<Name %r>' % self.name





@app.route('/in')
def hello_world():
    return render_template('in.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/everyday')
def everyday():
    return render_template('everyday.html')

#a=requests.post("https://gtdofdream.herokuapp.com/info/",data={'foo':'bar','input':'yangming is here'})

'''
#python flask deal with flask post
# requests.post('http://:5000/info',data={'user':'yangming','userinput':'yangming is here','content':'yangming'}).text
@app.route('/info',methods=['GET', 'POST'])
def info():
    print("i have no word")
    if request.method == 'POST':
        username = request.values.get('user')
        print(username)
        #req_data = request.get_json()
        content = request.values.get('foo')
        #print(content)
        userinput = request.values.get('input')
        taskcontent = task(str(userinput)
    db.session.add(taskcontent)    
    db.session.commit()    
    content = "yangming"
    a = {'test':'yangming is hereko','userinput':str(userinput),'time':str(time.time()),'user':str(username)}
    #print(content)
    #print(userinput)
    return json.dumps(a)

'''
@app.route('/info',methods=['GET','POST'])
def information():
    if request.method == 'POST':
        content = request.values.get('input')
        print(content)
        content = task(content)
        print(content)
        return json.dumps({'content':str(content)})
  










@app.route('/test')
def info1():

    a={'test':'yangming is hereko','time':str(time.time())}

    return json.dumps(a)










@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
