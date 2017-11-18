from app import db
class User1(db.Model):
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