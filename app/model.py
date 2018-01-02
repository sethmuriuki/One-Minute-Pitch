from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    '''
    Category class define category per pitch
    '''
    __tablename__ = 'categories'

     # add columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    #save
    def save_category(self):
        '''
        function that saves a category
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        function that returns all data  from the categories after being queried
        '''
        categories = Category.query.all()
        return categories

#pitches
class Talks(db.Model):
    '''
    list all pitches in category
    '''
    all_pitches = []
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    category_id = db.relationship("Comments", backref = "talks", lazy = "dynamic")


    def save_pitch(self):
        '''
        save pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        talks.all_pitches.clear()

    @classmethod
    def get_pitches(cls,id):
        pitches = Talks.query.order_by(Talks.date_posted.desc()).filter_by(category_id=id).all()
        return pitches

