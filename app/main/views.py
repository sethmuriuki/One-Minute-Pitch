from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Category, User,Peptalk, Comments
from .. import db
from flask_login import login_required, current_user
from .forms import PeptalkForm,CommentForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    categories = Category.get_categories()
    title = 'Home - Welcome to One Minute Pitch'
    return render_template('index.html', title = title, categories = categories)

