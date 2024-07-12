from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from webapp.extensions import db, login



class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String(128))
    spent = db.Column(db.Float)
    entry_date = db.Column(db.String(128))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def if_name_is_empty(self):
        if self.category == "":
            return True
        else:
            return False

    def if_name_is_valid(self):
        if self.category != self.category.capitalize():
            return False 
        else:
            return True

    def date_time_now(self):
        if self.date == datetime.utcnow():
            return True
        else:
            return False

    def __repr__(self):
        return 'Entry - {}'.format(self.category)



class Users(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    entry = db.relationship('Entry',backref='author',lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return str(self.id)

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))
    