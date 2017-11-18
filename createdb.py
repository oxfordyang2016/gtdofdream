from app import db
# from models import BlogPost

class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name




# create the database and the db table
db.create_all()

# insert data
db.session.add(User1("Good", "I\'m good."))
db.session.add(User1("Well", "I\'m well."))
# db.session.add(BlogPost("Excellent", "I\'m excellent."))
# db.session.add(BlogPost("Okay", "I\'m okay."))
# db.session.add(BlogPost("postgres", "we setup a local postgres instance"))

# commit the changes
db.session.commit()