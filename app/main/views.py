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

# Dynamic routing for pitches
@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PeptalkForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        # user = current_user._get_current_object()
        new_pitch = Peptalk(content=content,user_id=current_user.id,category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))

    title = 'New pitch'
    return render_template('new_pitches.html', title = title, pitch_form = form)