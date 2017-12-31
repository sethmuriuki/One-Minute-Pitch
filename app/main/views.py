from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Category, User,Peptalk, Comments
from .. import db
from flask_login import login_required, current_user
from .forms import PeptalkForm,CommentForm