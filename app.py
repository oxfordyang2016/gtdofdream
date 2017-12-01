import os,time,json
from datetime import datetime
from flask import Flask, request,jsonify
from flask import render_template
try:
    from flask.ext.sqlalchemy import SQLAlchemy
except:
    pass    
#in procfile to specify the python run the app
#web: FLASK_APP = server.py python -m flask run --host=0.0.0.0 --port=$PORT
app = Flask(__name__)
try:    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except:
    pass
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
try:
    db = SQLAlchemy(app)
except:
    pass

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

    task = db.Column(db.String(120), unique=True)

    def __init__(self, task):
        self.task = task
        self.date = str(datetime.now())


    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/xiajian')
def law():
    return render_template('youdu.html')




@app.route('/gtdcli'):
def gtdcli():
    print("i have no word")
    if request.method == 'POST':
        inboxthing = request.values.get('inbox')
        inputtime = request.values.get('input-time'))
        taskstatus = request.values.get('task-status')
        plantime = request.values.get('plantime')
        print(inboxthing)
        return json.dumps({'status':'u have uploaded successfully'})
    else:
        return json.dumps({'status':'upload fail'})



@app.route('/dream')
def dream():
    return render_template('fiveyearplan.html')



@app.route('/deadlist')
def deadlist():
    return render_template('fiveyearplan.html')





@app.route('/in')
def hello_world():
    return render_template('in.html')


@app.route('/todoist')
def todo():
    return render_template('toist.html')



@app.route('/all')
def all():
    return render_template('all.html')


@app.route('/task')
def task():
    return render_template('task.html')




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
        #user = User(str(time.time()), str(content)+str(time.time()))
        #db.session.add(user)
        taskcontent = task(str(content))
        db.session.add(taskcontent)
        db.session.commit()
        print(content)
        #all_users = User.query.all()
        #print(all_users)
        '''
        for k in all_users:
            print(str(k.email)+'email')
        '''    
        #content = task(content)
        #print(content)
        return json.dumps({'content':str(content),'time':str(time.time())})

#ios requests http post  
@app.route('/info1',methods=['GET','POST'])
def information1():
    if request.method == 'POST':
        info = []
        try:
            print(request.json)
        except:
             info1 = "request json have no data"
             info.append(info1)    
        try:
            a=request.get_data()
            print(a)
            taskcontent = task(str(a))
            db.session.add(taskcontent)
            db.session.commit()
            try:
                with open('./templates/freewriting.md','a') as f:
                    f.write(str(a))
            except:
                print("write file error")     
        except:
            a = ("request.data() error")
            info.append(a)    
        try:
            print(json.loads(request.data))
        except:
            b = "json parser fail" 
            info.append(b)   
        #content = request.values.get('input')
        #user = User(str(time.time()), str(content)+str(time.time()))
        #db.session.add(user)
        #taskcontent = task(str(content))
        #db.session.add(taskcontent)
        #db.session.commit()
        #print(content)
        #all_users = User.query.all()
        #print(all_users)
        '''
        for k in all_users:
            print(str(k.email)+'email')
        '''    
        #content = task(content)
        #print(content)
        return jsonify(input1=str("yangmingis=====here"),info1 =str(info))








@app.route('/test')
def info1():

    a={'test':'yangming is hereko','time':str(time.time())}

    return json.dumps(a)


@app.route('/testpost')
def info2():

    a={'test':'++++++++++++','time':str(time.time())}

    return json.dumps(a)






@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
