from app import db
# from models import BlogPost
from models import User1,task


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