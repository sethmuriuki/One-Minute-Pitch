from flask import render_template,redirect,url_for,abort
from . import main
from ..model import Category
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
        new_pitch = Talks(content=content,user_id=current_user.id,category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))

    title = 'New pitch'
    return render_template('new_pitches.html', title = title, pitch_form = form)

# Dynamic routing for one pitch
@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def single_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''

    pitches = Talks.query.get(id)

    if pitches is None:
        abort(404)

    comment = Comments.get_comments(id)
    title = 'Comment Section'
    return render_template('pitch.html', title = title, pitches = pitches, comment = comment)

# Dynamic routing for comment section
@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Talks.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment_section_id = form.comment_section_id.data
        new_comment = Comments(comment_section_id=comment_section_id,user_id=current_user.id,pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.category', id = pitches.id))

    title = 'New Comment'
    return render_template('comments.html', title = title, comment_form = form)